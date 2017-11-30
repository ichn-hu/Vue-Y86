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


def writebackRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    cc.Stat = SAOK if W.stat in [SBUB] else W.stat
    if not W.bubble and not W.stall:
        reg.write(W.dstE, W.valE, W.dstM, W.valM)
    


        
    