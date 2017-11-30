from const import *
from .misc import swichEndian, split2chunks


def decodeUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
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

    ret = {
        'stall': D.stall,
        'bubble': D.bubble,
        'stat': D.stat,
        'icode': D.icode,
        'ifun': D.ifun,
        'valC': D.valC,
        'valP': D.valP,
        'rA': D.rA,
        'rB': D.rB
    }
    return ret


def decodeRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    """
    Write or read data from register file, need to deal with 
    data-forwarding. 
    """

    if D.icode in [IRRMOVL, IRMMOVL, IOPL, IPUSHL]:
        d.srcA = D.rA
    elif D.icode in [IPOPL, IRET]:
        d.srcA = RESP
    elif D.icode in [ILEAVE]:
        d.srcA = REBP
    else:
        d.srcA = RNONE

    if D.icode in [IOPL, IRMMOVL, IMRMOVL, IIADDL]:
        d.srcB = D.rB
    elif D.icode in [IPUSHL, IPOPL, ICALL, IRET]:
        d.srcB = RESP
    else:
        d.srcB = RNONE

    if D.icode in [IRRMOVL, IIRMOVL, IOPL, IIADDL]:
        d.dstE = D.rB
    elif D.icode in [IPUSHL, IPOPL, ICALL, IRET, ILEAVE]:
        d.dstE = RESP
    else:
        d.dstE = RNONE

    if D.icode in [IMRMOVL, IPOPL]:
        d.dstM = D.rA
    elif D.icode in [ILEAVE]:
        d.dstM = REBP
    else:
        d.dstM = RNONE

    d.rvalA, d.rvalB = reg.read(d.srcA, d.srcB)

    if D.icode in [ICALL, IJXX]:
        d.valA = D.valP
        # 对于call和jmp, 不需要从寄存器读, 用valA代替valP
    elif d.srcA in [e.dstE]:
        d.valA = e.valE
        # ALU计算结果. add $eax, $ebx; mov %ebx, %ecx
    elif d.srcA in [M.dstM]:
        d.valA = m.valM
        # 内存读取结果. mov ($eax), %ebx; mov %ebx, %ecx
    elif d.srcA in [M.dstE]:
        d.valA = M.valE
        # 上上句是计算. add $eax, $ebx; xor %ecx, %ecx; mov %ebx, %ecx
    elif d.srcA in [W.dstM]:
        d.valA = W.valM
        # 上上句是读内存
    elif d.srcA == W.dstE:
        d.valA = W.valE
        # 上上上句是计算
    else:
        d.valA = d.rvalA

    if d.srcB in [e.dstE]:
        d.valB = e.valE # forward, 
    elif d.srcB in [M.dstM]:
        d.valB = m.valM
    elif d.srcB in [M.dstE]:
        d.valB = M.valE
    elif d.srcB in [W.dstM]:
        d.valB = W.valM
    elif d.srcB in [W.dstE]:
        d.valB = W.valE
    else:
        d.valA = d.rvalA

    ret = {
        '_srcA': d.srcA,
        '_srcB': d.srcB,
        '_valA': d.valA,
        '_valB': d.valB,
        '_dstE': d.dstE,
        '_dstM': d.dstM
    }
    return ret

