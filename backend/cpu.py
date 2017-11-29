"""
CPU implemention, including all the control logics
"""
import os
from const import *
from register import Register
from memory import Memory
from misc import split2chunks, swichEndien
import pipe
from pipe import F, f, D, d, E, e, M, m, W, w

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
    f.valP = swichEndien(hex(int(swichEndien(f.pc), 16) \
                + 1 * int(f.need_regid) \
                + 4 * int(f.need_valC)))


    if f.need_valC:
        f.valC = mem.read(f.pc + 1 + int(f.need_regid), 4)
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
    pass

def decodeRun():
    pass
def decodeUpdate():
    pass

def excuteRun():
    pass
def excuteUpdate():
    pass

def memoryRun():
    pass
def memoryUpdate():
    pass

def writeBackRun():
    pass
def writeBackUpdate():
    pass

def init(instr):
    mem.load(instr)

if __name__ == "__main__":
    os.chdir("C:\\Users\\ichne\\Documents\\Vue-Y86\\backend")
    instr = open("sample.yo", "r").read()
    init(instr)
    pipe.init()
    fetchRun()