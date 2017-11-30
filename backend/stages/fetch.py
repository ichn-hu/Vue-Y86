from const import *
from .misc import swichEndian, split2chunks, toInteger, int16


def fetchRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    ret = {}

    if M.icode in [IJXX] and not M.Cnd:
        f.pc = M.valA
        # 这里的valA就是IJXX在decode时的valP
    elif M.icode in [IRET]:
        f.pc = W.valM
    else:
        f.pc = F.predPC

    try:
        f.icode, f.ifun = split2chunks(mem.read(toInteger(f.pc), 1), 1)
        f.icode = int16(f.icode)
        f.ifun = int16(f.ifun)
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

    f.need_regid = f.icode in [IRRMOVL, IOPL, IPUSHL, IPOPL,
                               IIRMOVL, IRMMOVL, IMRMOVL]
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

    ret['_pc'] = f.pc
    ret['_stat'] = f.stat
    ret['_icode'] = f.icode
    ret['_ifun'] = f.ifun
    ret['_imem_error'] = f.imem_error
    ret['_need_regid'] = f.need_regid
    ret['_instr_valid'] = f.instr_valid
    ret['_valP'] = f.valP
    ret['_valC'] = f.valC
    ret['_rA'] = f.rA
    ret['_rB'] = f.rB
    return ret


def fetchUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    ret = []
    F.bubble = False
    if (E.icode in [IMRMOVL, IPOPL] and E.dstM in [d.srcA, d.srcB]) \
        or IRET in [D.icode, E.icode, M.icode]:
        F.stall = True
        # load interloak
        # 或者无法预测
    else:
        F.stall = False

    if not F.bubble and not F.stall:
        F.predPC = f.predPC

    D.stall = True if E.icode in [IMRMOVL, IPOPL] \
        and E.dstM in [d.srcA, d.srcB] else False
        # load interlock
    D.bubble = True if (E.icode in [IJXX] and not e.Cnd) \
        or (not (E.icode in [IMRMOVL, IPOPL] and E.dstM in [d.srcA, d.srcB])
            and IRET in [D.icode, E.icode, M.icode]) else False
        # 分支预测错误
    if not D.stall and not D.bubble:
        D.stat = f.stat
        D.icode = f.icode
        D.ifun = f.ifun
        D.valC = f.valC
        D.valP = f.valP
        D.rA = f.rA
        D.rB = f.rB
    if D.bubble:
        D.stat = SBUB
        D.icode = INOP
        D.ifun = FNONE
        D.valC = ZERO
        D.valP = ZERO
        D.rA = RNONE
        D.rB = RNONE
