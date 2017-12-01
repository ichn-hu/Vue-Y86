from const import *
from misc import toInteger


def memory(cur, nxt, mem):
    if cur.M.icode in [IRMMOVL, IPUSHL, ICALL, IMRMOVL]:
        mem_addr = cur.M.valE
    elif cur.M.icode in [IPOPL, IRET]:
        mem_addr = cur.M.valA
    else:
        mem_addr = None

    mem_read = True if cur.M.icode in [IMRMOVL, IPOPL, IRET] else False
    mem_write = True if cur.M.icode in [IRMMOVL, IPUSHL, ICALL] else False
    dmem_error = False
    valM = None
    if mem_read:
        try:
            valM = mem.read(toInteger(mem_addr), 4)
        except:
            dmem_error = True
    if mem_write:
        try:
            mem.write(toInteger(mem_addr), cur.M.valA)
        except:
            dmem_error = True
    #if M.icode in [IMRMOVL]:
    #    print(m.valM, regName[M.dstM])

    nxt.W = cur.Reg(**{
        'stat': SADR if dmem_error else cur.M.stat,
        'icode': cur.M.icode,
        'valE': cur.M.valE,
        'valM': valM,
        'dstE': cur.M.dstE,
        'dstM': cur.M.dstM,
        'ins': cur.M.ins
    })
