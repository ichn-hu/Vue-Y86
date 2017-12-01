from const import *
from misc import swichEndian, split2chunks


def decode(cur, nxt, reg):
    srcA = RNONE
    if cur.D.icode in [IRRMOVL, IRMMOVL, IOPL, IPUSHL]:
        srcA = cur.D.rA
    elif cur.D.icode in [IPOPL, IRET]:
        srcA = RESP
    srcB = RNONE
    if cur.D.icode in [IOPL, IRMMOVL, IMRMOVL]:
        srcB = cur.D.rB
    elif cur.D.icode in [IPUSHL, IPOPL, ICALL, IRET]:
        srcB = RESP

    dstE = RNONE
    if cur.D.icode in [IRRMOVL, IIRMOVL, IOPL]:
        dstE = cur.D.rB
    elif cur.D.icode in [IPUSHL, IPOPL, ICALL, IRET]:
        dstE = RESP
    dstM = RNONE
    if cur.D.icode in [IMRMOVL, IPOPL]:
        dstM = cur.D.rA

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
        # 理论上讲应该写回了

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
        'srcB': srcB,
        'ins': cur.D.ins
    })