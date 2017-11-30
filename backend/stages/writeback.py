from const import *

def writebackRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    pass
    

def writebackUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    W.bubble = False
    W.stall = True if W.stat in [SADR, SINS, SHLT] else False
    if not W.bubble and not W.stall:
        reg.write(W.dstE, W.valE, W.dstM, W.valM)
        cc.Stat = SAOK if W.stat in [SBUB] else W.stat
    