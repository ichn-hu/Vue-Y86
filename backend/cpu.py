"""
CPU implemention, including all the control logics
"""
import os

import pipe
from const import *
from memory import Memory
from misc import split2chunks, swichEndian
from pipe import D, E, F, M, W, d, e, f, m, w, cc, aluAdd, aluSub, aluXor, aluAnd
from register import Register

reg = Register()
mem = Memory()

def fetchRun():
    if M.icode == IJXX and not M.Cnd:
        f.pc = M.valA
    elif M.icode == IRET:
        f.pc = W.valM
    else:
        f.pc = F.predPC

    try:
        f.icode, f.ifun = split2chunks(mem.read(f.pc, 1), 1)
    except:
        f.imem_error = True
        f.icode = INOP
        f.ifun = FNONE
    
    f.instr_valid = f.ifun in [ INOP, IHALT, IRRMOVL, IIRMOVL, IRMMOVL, IMRMOVL, \
                                IOPL, IJXX, ICALL, IRET, IPUSHL, IPOPL]
    
    if f.imem_error:
        f.stat = SADR
    elif not f.instr_valid:
        f.stat = SINS
    elif f.icode == IHALT:
        f.stat = SHLT
    else:
        f.stat = SAOK
    
    f.need_regid = f.icode in [IRRMOVL, IRMMOVL, IMRMOVL, IIRMOVL, IPUSHL, IPOPL, IIADDL]
    f.need_valC = f.icode in [IIRMOVL, IRMMOVL, IMRMOVL, IJXX, ICALL, IIADDL]   
    f.valP = swichEndian(hex(int(swichEndian(f.pc), 16) \
                + 1 * int(f.need_regid) \
                + 4 * int(f.need_valC)))


    if f.need_valC:
        f.valC = mem.read(int(swichEndian(f.pc), 16) + 1 + int(f.need_regid), 4)
    else:
        f.valC = None

    if f.icode in [IJXX, ICALL]:
        f.predPC = f.valC
    else:
        f.predPC = f.valP

    if f.need_regid:
        f.rA, f.rB = split2chunks(mem.read(f.pc + 1, 1), 1)
    else:
        f.rA, f.rB = RNONE, RNONE

def fetchUpdate():
    F.predPC = f.predPC
    D.valC = f.valC
    D.valP = f.valP
    D.rA = f.rA
    D.rB = f.rB
    D.icode = f.icode
    D.ifun = f.ifun
    D.stat = f.stat

def decodeRun():
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

def decodeUpdate():
    D.stat = f.stat
    D.icode = f.icode
    D.ifun = f.ifun
    D.rA = f.rA
    D.rB = f.rB
    D.valC = f.valC
    D.valP = f.valP

def excuteRun():
    if E.icode in (IRRMOVL, IOPL, ILEAVE):
        e.valA = E.valA
    elif E.icode in (IIRMOVL, IRMMOVL, IMRMOVL, IIADDL):
        e.valA = E.valC
    elif E.icode in (ICALL, IPUSHL):
        e.valA = -4
    elif E.icode in (IRET, IPOPL):
        e.valA = 4
    else:
        e.valA = 0
    
    if E.icode in (IRMMOVL, IMRMOVL, IOPL, ICALL, \
                   IPUSHL, IRET, IPOPL, IIADDL):
        e.valB = E.valB
    elif E.icode == ILEAVE:
        e.valB = 4
    else:
        e.valB = 0
    
    if E.icode == IOPL:
        e.aluFun = int(E.ifun)
    else:
        e.aluFun = AADD

    e.aluA = swichEndian(e.valA)
    e.aluB = swichEndian(e.valB)

    e.set_cc = E.icode in (IOPL, IIADDL) and \
               m.stat not in (SADR, SINS, SHLT) and \
               W.stat not in (SADR, SINS, SHLT)

    if e.aluFun == AADD:
        e.aluRes = aluAdd(e.aluA, e.aluB, e.set_cc, cc)
    elif e.aluFun == ASUB:
        e.aluRes = e.aluA - e.aluB
    elif e.aluFun == AAND:
        e.aluRes = e.aluA & e.aluB
    else:
        e.aluRes = e.aluA ^ e.aluB
    
    
    
    # TODO: correct errors below
    if e.set_cc:
        cc.ZF = 1 if e.aluRes == 0 else 0
        cc.SF = 1 if e.aluRes < 0 else 0
        if (e.aluFun == AADD) and \
            ((e.aluB > 0 and e.aluA > 0 and e.aluRes < 0) or \
              e.aluB < 0 and e.aluB < 0 and e.aluRes > 0):
            cc.OF = 1
        if (e.aluFun == ASUB) and \
            ((e.aluB > 0 and e.aluA < 0 and e.aluRes < 0) or \
              e.aluB < 0 and e.aluB > 0 and e.aluRes > 0):
            cc.OF = 1
    
    # TODO: correct Cnd
    e.Cnd = e.set_cc
    

def excuteUpdate():
    if (E.icode == IJXX and not e.Cnd) or \
        E.icode in (IMRMOVL, IPOPL) and \
        E.dstM in (d.srcA, d.srcB):
        E.icode = INOP
        E.ifun = FNONE
        E.valC = 0x0
        E.valA = 0x0
        E.valB = 0x0
        E.dstE = RNONE
        E.dstM = RNONE
        E.srcA = RNONE
        E.srcB = RNONE
        E.stat = 'BUB'
        return
    E.stat = D.stat
    E.icode = D.icode
    E.ifun = D.ifun
    E.valC = D.valC
    E.valA = d.valA
    E.valB = d.valB
    E.dstE = d.dstE
    E.dstM = d.dstM
    E.srcA = d.srcA
    E.srcB = d.srcB

def memoryRun():
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
            m.valM = mem.read(M.valE, 4)
        except:
            m.dmem_error = True
    if m.mem_write:
        try:
            mem.write(M.valE, M.valA)
        except:
            m.dmem_error = True
    m.stat = SADR if m.dmem_error else M.stat

    

def memoryUpdate():
    M.stat = E.stat
    M.icode = E.icode
    M.Cnd = e.Cnd
    M.valE = e.valE
    M.valA = E.valA
    M.dstE = e.dstE
    M.dstM = E.dstM

def writeBackRun():
    reg.write(W.dstE, W.valE, W.dstM, W.valM)

def writeBackUpdate():
    W.stat = m.stat

def init(instrCode):
    mem.load(instrCode)

if __name__ == "__main__":
    os.chdir("C:\\Users\\ichne\\Documents\\Vue-Y86\\backend")
    instrCode = open("sample.yo", "r").read()
    init(instrCode)
    pipe.init()
    fetchRun()
