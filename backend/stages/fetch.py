from const import *
from .misc import swichEndian, split2chunks, toInteger, int16


def fetchRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    info = {}
    info['stageName'] = 'fetchRun'

    if M.icode in [IJXX] and not M.Cnd:
        f.pc = M.valA
        # 这里的valA就是IJXX在decode时的valP
    elif M.icode in [IRET]:
        f.pc = W.valM
    else:
        f.pc = F.predPC

    info['pc'] = f.pc

    try:
        f.icode, f.ifun = split2chunks(mem.read(toInteger(f.pc), 1), 1)
        f.icode = int16(f.icode)
        f.ifun = int16(f.ifun)
    except:
        f.imem_error = True
        f.icode = INOP
        f.ifun = FNONE

    info['icode'] = f.icode
    info['ifun'] = f.ifun

    f.instr_valid = f.ifun in [INOP, IHALT, IRRMOVL, IIRMOVL, IRMMOVL, IMRMOVL,
                               IOPL, IJXX, ICALL, IRET, IPUSHL, IPOPL]

    if f.imem_error:
        f.stat = SADR
    elif not f.instr_valid:
        f.stat = SINS
    elif f.icode == IHALT:
        f.stat = SHLT
    else:
        f.stat = SAOK

    f.need_regid = f.icode in [IRRMOVL, IRMMOVL, IMRMOVL,
                               IIRMOVL, IPUSHL, IPOPL, IIADDL]
    f.need_valC = f.icode in [IIRMOVL, IRMMOVL, IMRMOVL,
                              IJXX, ICALL, IIADDL]
    f.valP = swichEndian(hex(toInteger(f.pc) + 1
                             + 1 * int(f.need_regid)
                             + 4 * int(f.need_valC)))

    if f.need_valC:
        f.valC = mem.read(toInteger(f.pc) +
                          1 + int(f.need_regid), 4)
    else:
        f.valC = None

    if f.icode in [IJXX, ICALL]:
        f.predPC = f.valC
    else:
        f.predPC = f.valP

    if f.need_regid:
        f.rA, f.rB = split2chunks(mem.read(toInteger(f.pc) + 1, 1), 1)
        f.rA = int16(f.rA)
        f.rB = int16(f.rB)
    else:
        f.rA, f.rB = RNONE, RNONE

    return info


def fetchUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    D.stat = f.stat
    D.icode = f.icode
    D.ifun = f.ifun
    F.predPC = f.predPC
    D.valC = f.valC
    D.valP = f.valP
    D.rA = f.rA
    D.rB = f.rB
