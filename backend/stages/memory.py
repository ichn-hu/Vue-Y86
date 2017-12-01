from const import *
from misc import toInteger


def memoryUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
        
    M.stall = False
    M.bubble = True if m.stat in [SADR, SINS, SHLT] \
        or W.stat in [SADR, SINS, SHLT] else False

    if not M.stall and not M.bubble:
        M.stat = E.stat
        M.ifun = E.ifun
        M.icode = E.icode
        M.Cnd = e.Cnd
        M.valE = e.valE
        M.valA = e.valA
        M.dstE = e.dstE
        M.dstM = E.dstM
    if M.bubble:
        M.stat = SBUB
        M.ifun = FNONE
        M.icode = INOP
        M.Cnd = False
        M.valE = ZERO
        M.valA = ZERO
        M.dstE = RNONE
        M.dstM = RNONE

    
    ret = {
        'stall': M.stall,
        'bubble': M.bubble,
        'stat': M.stat,
        'ifun': M.ifun,
        'icode': M.icode,
        'Cnd': M.Cnd,
        'valE': M.valE,
        'valA': M.valA,
        'dstE': M.dstE,
        'dstM': M.dstM
    }
    return ret


def memoryRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    if M.icode in [IRMMOVL, IPUSHL, ICALL, IMRMOVL]:
        m.mem_addr = M.valE
    elif M.icode in [IPOPL, IRET]:
        m.mem_addr = M.valA
    else:
        m.mem_addr = None

    m.mem_read = True if M.icode in [IMRMOVL, IPOPL, IRET] else False
    m.mem_write = True if M.icode in [IRMMOVL, IPUSHL, ICALL] else False
    m.dmem_error = False
    if m.mem_read:
        try:
            m.valM = mem.read(toInteger(m.mem_addr), 4)
        except:
            m.dmem_error = True
    if m.mem_write:
        try:
            mem.write(toInteger(m.mem_addr), M.valA)
        except:
            m.dmem_error = True
    #if M.icode in [IMRMOVL]:
    #    print(m.valM, regName[M.dstM])

    m.stat = SADR if m.dmem_error else M.stat

    ret = {
        '_mem_addr': m.mem_addr,
        '_mem_read': m.mem_read,
        '_mem_write': m.mem_write,
        '_dmem_error': m.dmem_error,
        '_stat': m.stat
    }
    return ret
