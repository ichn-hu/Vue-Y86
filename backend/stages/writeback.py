from const import *


def writebackUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
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
    
    ret = {
        'bubble': W.bubble,
        'stall': W.stall,
        'stat': W.stat,
        'icode': W.icode,
        'valE': W.valE,
        'valM': W.valM,
        'dstE': W.dstE,
        'dstM': W.dstM
    }
    return ret


def writebackRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    w.dstE = W.dstE
    w.valE = W.valE
    w.dstM = W.dstM
    w.valM = W.valM
    w.Stat = SAOK if W.stat in [SBUB] else W.stat
    # TODO: whether the if need to be removed?
    # if not W.bubble and not W.stall:
    reg.write(w.dstE, w.valE, w.dstM, w.valM)
    return {'_Stat': w.Stat, '_dstE': w.dstE,
            '_valE': w.valE, '_dstM': w.dstM, '_valM': w.valM}
