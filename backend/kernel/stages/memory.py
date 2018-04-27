from kernel.const import *
from kernel.misc import toInteger, swichEndian


def memory(cur, nxt, mem):
    op = []

    if cur.M.icode in [IRMMOVL, IPUSHL, ICALL, IMRMOVL]:
        mem_addr = cur.M.valE
    elif cur.M.icode in [IPOPL, IRET]:
        mem_addr = cur.M.valA
    else:
        mem_addr = None

    mem_read = True if cur.M.icode in [IMRMOVL, IPOPL, IRET] else False
    mem_write = True if cur.M.icode in [IRMMOVL, IPUSHL, ICALL] else False
    dmem_error = False
    valM = VNONE
    if mem_read:
        try:
            valM = mem.read(toInteger(mem_addr), 4)
            op.append('Memory reads {0}'.format(swichEndian(valM)))
        except:
            dmem_error = True
            op.append('Error: read from {0}'.format(swichEndian(mem_addr)))
    if mem_write:
        try:
            mem.write(toInteger(mem_addr), cur.M.valA)
            op.append('Memory writes {0}'.format(swichEndian(cur.M.valA)))
        except:
            dmem_error = True
            op.append('Error: write to {0}'.format(swichEndian(mem_addr)))
    #if M.icode in [IMRMOVL]:
    #    print(m.valM, regName[M.dstM])

    cur.M.__dict__.update(**{
        'operation': op
    })
    nxt.W.__dict__.update(**{
        'ins': cur.M.ins,
        'stat': SADR if dmem_error else cur.M.stat,
        'icode': cur.M.icode,
        'valE': cur.M.valE,
        'valM': valM,
        'dstE': cur.M.dstE,
        'dstM': cur.M.dstM,
    })
