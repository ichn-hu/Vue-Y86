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
from stages.fetch import fetchRun, fetchUpdate
from stages.memory import memoryRun, memoryUpdate
from stages.decode import decodeRun, decodeUpdate
from stages.execute  import executeRun, executeUpdate
from stages.writeback import writebackRun, writebackUpdate

reg, mem = None, None

def init(instrCode):
    global reg, mem
    reg = Register()
    mem = Memory()
    mem.load(instrCode)
    pipe.init()

def run():
    while W.stat == SAOK:
        


if __name__ == "__main__":
    os.chdir("C:\\Users\\ichne\\Documents\\Vue-Y86\\backend")
    instrCode = open("sample.yo", "r").read()
    init(instrCode)
    pipe.init()
