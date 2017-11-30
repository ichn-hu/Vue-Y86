from const import *
from .misc import swichEndian, split2chunks


def decodeRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    """
    Write or read data from register file, need to deal with 
    data-forwarding. 
    """
    info = {}
    info["stageName"] = "decodeRun"

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

    info['srcA'] = d.srcA
    info['srcB'] = d.srcB
    info['stat'] = D.stat

    return info


def decodeUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    info = {}
    info['stageName'] = 'decodeUpdate'

    E.stall = False
    E.bubble = True if (E.icode in [IJXX] and not e.Cnd) \
        or (E.icode in [IMRMOVL, IPOPL] and E.dstM in [d.srcA, d.srcB]) \
        else False

    if not E.stall and not E.bubble:
        E.stat = D.stat
        E.icode = D.icode
        E.ifun = D.ifun
        E.valC = D.valC
        E.srcA = d.srcA
        E.srcB = d.srcB
        E.valA = d.valA
        E.valB = d.valB
        E.dstE = d.dstE
        E.dstM = d.dstM
    
    if E.bubble:
        E.stat = SBUB
        E.icode = INOP
        E.ifun = FNONE
        E.valC = ZERO
        E.srcA = RNONE
        E.srcB = RNONE
        E.valA = ZERO
        E.valB = ZERO
        E.dstE = RNONE
        E.dstM = RNONE
        

    info['stat'] = E.stat
    # return info
