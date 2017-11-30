from const import *

def writebackRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    reg.write(W.dstE, W.valE, W.dstM, W.valM)

def writebackUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    W.stat = m.stat