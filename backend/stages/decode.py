from const import *
from misc import swichEndian, split2chunks


def decodeUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):

    D.stall = True if E.icode in [IMRMOVL, IPOPL] \
        and E.dstM in [srcA, srcB] else False
        # load interlock
    D.bubble = True if (E.icode in [IJXX] and not e.Cnd) \
        or (not (E.icode in [IMRMOVL, IPOPL] and E.dstM in [srcA, srcB])
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

def decode(cur, nxt, reg):
    srcA = RNONE
    if cur.D.icode in [IRRMOVL, IRMMOVL, IOPL, IPUSHL]:
        srcA = cur.D.rA
    elif cur.D.icode in [IPOPL, IRET]:
        srcA = RESP
    elif cur.D.icode in [ILEAVE]:
        srcA = REBP
    srcB = RNONE
    if cur.D.icode in [IOPL, IRMMOVL, IMRMOVL, IIADDL]:
        srcB = cur.D.rB
    elif cur.D.icode in [IPUSHL, IPOPL, ICALL, IRET]:
        srcB = RESP

    dstE = RNONE
    if cur.D.icode in [IRRMOVL, IIRMOVL, IOPL, IIADDL]:
        dstE = cur.D.rB
    elif cur.D.icode in [IPUSHL, IPOPL, ICALL, IRET, ILEAVE]:
        dstE = RESP
    dstM = RNONE
    if cur.D.icode in [IMRMOVL, IPOPL]:
        dstM = cur.D.rA
    elif cur.D.icode in [ILEAVE]:
        dstM = REBP

    valA, valB = reg.read(srcA, srcB)

    if cur.D.icode in [ICALL, IJXX]:
        valA = cur.D.valP
        # 对于call和jmp, 不需要从寄存器读, 用valA代替valP
    elif srcA in [nxt.M.dstE]:
        valA = nxt.M.valE
        # ALU计算结果. add $eax, $ebx; mov %ebx, %ecx
        # 当前状态的e.valE就是下个状态的M.valE
    elif srcA in [cur.M.dstM]:
        valA = nxt.W.valM
        # 内存读取结果. mov ($eax), %ebx; mov %ebx, %ecx
        # 当前状态的m.valM就是下个状态的W.valM
    elif srcA in [cur.M.dstE]:
        valA = cur.M.valE
        # 上上句是计算. add $eax, $ebx; xor %ecx, %ecx; mov %ebx, %ecx
    elif srcA in [cur.W.dstM]:
        valA = cur.W.valM
        # 上上句是读内存
    elif srcA == cur.W.dstE:
        valA = cur.W.valE
        # 上上上句是计算

    if srcB in [nxt.M.dstE]:
        valB = nxt.M.valE # forward, 
    elif srcB in [cur.M.dstM]:
        valB = nxt.W.valM
    elif srcB in [cur.M.dstE]:
        valB = cur.M.valE
    elif srcB in [cur.W.dstM]:
        valB = cur.W.valM
    elif srcB in [cur.W.dstE]:
        valB = cur.W.valE
    
    nxt.E = cur.Reg(**{
        'stat': cur.D.stat,
        'icode': cur.D.icode,
        'ifun': cur.D.ifun,
        'valC': cur.D.valC,
        'valA': valA,
        'valB': valB,
        'dstE': dstE,
        'dstM': dstM,
        'srcA': srcA,
        'srcB': srcB
    })