from const import *
from misc import swichEndian, split2chunks, toInteger, int16


def fetchUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
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

    return {'stall': F.stall, 'bubble': F.bubble, 'predPC': F.predPC}


def fetch(cur, nxt, mem):
    pc = cur.F.predPC

    if cur.M.icode in [IJXX] and not cur.M.Cnd:
        pc = cur.M.valA
        # 这里的valA就是IJXX在decode时的valP
    elif cur.W.icode in [IRET]:
        pc = cur.W.valM

    try:
        icode, ifun = split2chunks(mem.read(toInteger(pc), 1), 1)
        icode = int16(icode)
        ifun = int16(ifun)
    except:
        imem_error = True
        icode = INOP
        ifun = FNONE

    instr_valid = ifun in [INOP, IHALT, IRRMOVL, IIRMOVL, IRMMOVL, IMRMOVL,
                           IOPL, IJXX, ICALL, IRET, IPUSHL, IPOPL]

    need_regid = icode in [IRRMOVL, IOPL, IPUSHL, IPOPL,
                           IIRMOVL, IRMMOVL, IMRMOVL]
    need_valC = icode in [IIRMOVL, IRMMOVL, IMRMOVL,
                          IJXX, ICALL, IIADDL]
    valP = swichEndian(hex(toInteger(pc) + 1
                           + 1 * int(need_regid)
                           + 4 * int(need_valC)))
    valC = None
    if need_valC:
        try:
            valC = mem.read(toInteger(pc) +
                        1 + int(need_regid), 4)
        except:
            imem_error = True

    rA, rB = RNONE, RNONE
    if need_regid:
        try:
            rA, rB = split2chunks(mem.read(toInteger(pc) + 1, 1), 1)
            rA = int16(rA)
            rB = int16(rB)
        except:
            imem_error = True

    if imem_error:
        stat = SADR
    elif not instr_valid:
        stat = SINS
    elif icode == IHALT:
        stat = SHLT
    else:
        stat = SAOK

    if icode in [IJXX, ICALL]:
        predPC = valC
    else:
        predPC = valP


    nxt.D = nxt.Reg(**{
        'icode': icode,
        'ifun': ifun,
        'stat': stat,
        'rA': rA,
        'rB': rB,
        'valC': valC,
        'valP': valP,
    })
    nxt.F = cur.Reg(**{
        'predPC': predPC
    })