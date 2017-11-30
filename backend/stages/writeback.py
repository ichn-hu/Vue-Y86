from const import *

def writebackRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    info = {}
    info['stageName'] = 'writebackRun'
    info['stat'] = W.stat
    return info
    

def writebackUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    W.bubble = False
    W.stall = True if W.stat in [SADR, SINS, SHLT] else False
    cc.Stat = SAOK if W.stat in [SBUB] else W.stat
    if not W.bubble and not W.stall:
        reg.write(W.dstE, W.valE, W.dstM, W.valM)
        
    