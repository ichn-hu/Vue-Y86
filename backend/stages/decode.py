from const import *
from misc import swichEndian, split2chunks

def decodeRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    """
    Write or read data from register file, need to deal with 
    data-forwarding. 
    """
    if D.icode in (IRRMOVL, IRMMOVL, IOPL, IPUSHL):
        d.srcA = D.rA
    elif D.icode in (IPOPL, IRET):
        d.srcA = RESP
    elif D.icode == ILEAVE:
        d.srcA = REBP
    else:
        d.srcA = RNONE
    
    if D.icode in (IOPL, IRMMOVL, IMRMOVL, IIADDL):
        d.srcB = D.rB
    elif D.icode in (IPUSHL, IPOPL, ICALL, IRET):
        d.srcB = RESP
    else:
        d.srcB = RNONE

    
    if D.icode in (IRRMOVL, IIRMOVL, IOPL, IIADDL):
        d.dstE = D.rB
    elif D.icode in (IPUSHL, IPOPL, ICALL, IRET, ILEAVE):
        d.dstE = RESP
    else:
        d.dstE = RNONE

    
    if D.icode in (IMRMOVL, IPOPL):
        d.dstM = D.rA
    elif D.icode == ILEAVE:
        d.dstM = REBP
    else:
        d.dstM = RNONE

    d.rvalA, d.rvalB = reg.read(d.srcA, d.srcB)

    if D.icode in (ICALL, IJXX):
        d.valA = D.valP
    elif d.srcA == e.dstE:
        d.valA = e.valE
    elif d.srcA == M.dstM:
        d.valA = m.valM
    elif d.srcA == M.dstE:
        d.valA = M.valE
    elif d.srcA == W.dstM:
        d.valA = W.valM
    elif d.srcA == W.dstE:
        d.valA = W.valE
    else:
        d.valA = d.rvalA

    if d.srcB == e.dstE:
        d.valB = e.valE
    elif d.srcB == M.dstM:
        d.valB = m.valM
    elif d.srcB == M.dstE:
        d.valB = M.valE
    elif d.srcB == W.dstM:
        d.valB = W.valM
    elif d.srcB == W.dstE:
        d.valB = W.valE
    else:
        d.valA = d.rvalA

def decodeUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):
    D.stat = f.stat
    D.icode = f.icode
    D.ifun = f.ifun
    D.rA = f.rA
    D.rB = f.rB
    D.valC = f.valC
    D.valP = f.valP