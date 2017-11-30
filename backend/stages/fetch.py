from const import *
from misc import swichEndian, split2chunks


def fetchRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    if M.icode == IJXX and not M.Cnd:
        f.pc = M.valA
        # 这里的valA就是IJXX在decode时的valP
    elif M.icode == IRET:
        f.pc = W.valM
    else:
        f.pc = F.predPC

    try:
        f.icode, f.ifun = split2chunks(mem.read(f.pc, 1), 1)
    except:
        f.imem_error = True
        f.icode = INOP
        f.ifun = FNONE

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
    f.valP = swichEndian(hex(int(swichEndian(f.pc), 16)
                             + 1 * int(f.need_regid)
                             + 4 * int(f.need_valC)))

    if f.need_valC:
        f.valC = mem.read(int(swichEndian(f.pc), 16) +
                          1 + int(f.need_regid), 4)
    else:
        f.valC = None

    if f.icode in [IJXX, ICALL]:
        f.predPC = f.valC
    else:
        f.predPC = f.valP

    if f.need_regid:
        f.rA, f.rB = split2chunks(mem.read(f.pc + 1, 1), 1)
    else:
        f.rA, f.rB = RNONE, RNONE


def fetchUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    D.stat = f.stat
    D.icode = f.icode
    D.ifun = f.ifun
    F.predPC = f.predPC
    D.valC = f.valC
    D.valP = f.valP
    D.rA = f.rA
    D.rB = f.rB
