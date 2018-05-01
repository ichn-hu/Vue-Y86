from kernel.const import *
from kernel.misc import swichEndian, split2chunks


def decode(cur, nxt, reg):
    op = []

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

    forward = False

    valid_valA = False

    if cur.D.icode in [ICALL, IJXX]:
        valA = cur.D.valP
        valid_valA = True
        # 对于call和jmp, 不需要从寄存器读, 用valA代替valP
    elif srcA in [nxt.M.dstE]:
        valA = nxt.M.valE
        # ALU计算结果. add $eax, $ebx; mov %ebx, %ecx
        # 当前状态的e.valE就是下个状态的M.valE
        forward = True
    elif srcA in [cur.M.dstM]:
        valA = nxt.W.valM
        forward = True
        # 内存读取结果. mov ($eax), %ebx; mov %ebx, %ecx
        # 当前状态的m.valM就是下个状态的W.valM
    elif srcA in [cur.M.dstE]:
        valA = cur.M.valE
        forward = True
        # 上上句是计算. add $eax, $ebx; xor %ecx, %ecx; mov %ebx, %ecx
    elif srcA in [cur.W.dstM]:
        valA = cur.W.valM
        forward = True
        # 上上句是读内存
    elif srcA == cur.W.dstE:
        valA = cur.W.valE
        forward = True
        # 上上上句是计算
        # 理论上讲应该写回了
    elif srcA != RNONE:
        op.append('Load {0} to {1} from register file'.format(swichEndian(valA), regName[srcA]))

    if forward and srcA != RNONE:
        op.append('Forward {0} to {1}'.format(swichEndian(valA), regName[srcA]))
        
    forward = False

    if srcB in [nxt.M.dstE]:
        forward = True
        valB = nxt.M.valE # forward, 
    elif srcB in [cur.M.dstM]:
        forward = True
        valB = nxt.W.valM
    elif srcB in [cur.M.dstE]:
        forward = True
        valB = cur.M.valE
    elif srcB in [cur.W.dstM]:
        forward = True
        valB = cur.W.valM
    elif srcB in [cur.W.dstE]:
        forward = True
        valB = cur.W.valE
    elif srcB != RNONE:
        op.append('Load {0} to {1} from register file'.format(swichEndian(valB), regName[srcB]))
    
    if forward and srcB != RNONE:
        op.append('Forward {0} to {1}'.format(swichEndian(valB), regName[srcB]))

    cur.D.__dict__.update(**{
        'operation': op
    })

    if srcA == RNONE and not valid_valA:
        valA = VNONE
    if srcB == RNONE:
        valB = VNONE

    nxt.E.__dict__.update(**{
        'ins': cur.D.ins,
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
