from const import *
from .misc import toInteger


def memoryRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    info = {}
    info['stageName'] = 'memoryRun'

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
    m.stat = SADR if m.dmem_error else M.stat
    info['stat'] = m.stat
    return info


def memoryUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):

    W.bubble = False
    W.stall = True if W.stat in [SADR, SINS, SHLT] else False

    if not W.stall and not W.bubble:
        W.stat = m.stat
        W.icode = M.icode
        W.valE = M.valE
        W.valM = m.valM
        W.dstE = M.dstE
        W.dstM = M.dstM
    
    if W.bubble:
        W.stat = SBUB
        W.icode = INOP
        W.valE = ZERO
        W.valM = ZERO
        W.dstE = RNONE
        W.dstM = RNONE
