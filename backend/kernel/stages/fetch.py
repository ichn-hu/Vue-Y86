from kernel.const import *
from kernel.misc import swichEndian, split2chunks, toInteger, int16, disassemble
import sys

def fetch(cur, nxt, mem, over):
    op = []
    if cur.M.icode in [IJXX] and not cur.M.Cnd:
        pc = cur.M.valA
        op.append('Select current PC {0} due to previous JMP misprediction'.format(swichEndian(pc)))
    elif cur.W.icode in [IRET]:
        pc = cur.W.valM
        op.append('Select current PC {0} due to previous RET'.format(swichEndian(pc)))
    else:
        pc = cur.F.predPC
        op.append('Select current PC {0} naturally'.format(swichEndian(pc)))
    
    imem_error = False
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
    valC = VNONE
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
        op.append('Error: memory address invalid')
    elif not instr_valid:
        stat = SINS
        op.append('Error: instruction invalid')
    elif icode == IHALT:
        stat = SHLT
        op.append('Halt')
    else:
        stat = SAOK


    if icode in [IJXX, ICALL]:
        predPC = valC
        op.append('Select next PC {0} due to JMP or CALL'.format(swichEndian(predPC)))
    else:
        predPC = valP
        op.append('Select next PC {0} naturally'.format(swichEndian(predPC)))

    ins = VNONE
    if stat in [SAOK, SHLT]:
        ins = swichEndian(pc) + ': ' + disassemble(icode, ifun, rA, rB, valC)
    cur.F.__dict__.update(**{
        'ins': ins,
        'operation': op
    })
    nxt.D.__dict__.update(**{
        'icode': icode,
        'ifun': ifun,
        'stat': stat,
        'rA': rA,
        'rB': rB,
        'valC': valC,
        'valP': valP,
        'ins': ins
    })
    nxt.F.__dict__.update(**{
        'predPC': predPC
    })
    #sys.exit(str(nxt.F.predPC))
    over.append("fetch")