"""
CPU implemention, including all the control logics
"""
import os
from const import *
from register import Register
from memory import Memory
from misc import split2chunks
import pipe
from pipe import F, f, D, d, E, e, M, m, W, w

reg = Register()
mem = Memory()

def fetchRun():
    
    if M.icode == IJXX and not M.Cnd:
        f.pc = M.valA
    elif M.icode == IRET:
        f.pc = W.valM
        

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