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



def init(instr):
    mem.load(instr)

if __name__ == "__main__":
    os.chdir("C:\\Users\\ichne\\Documents\\Vue-Y86\\backend")
    instr = open("sample.yo", "r").read()
    init(instr)
    pipe.init()