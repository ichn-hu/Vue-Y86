"""
CPU implemention, including all the control logics
"""
import os
import io

import pipe
from const import *
from memory import Memory
from stages.misc import split2chunks, swichEndian
from pipe import D, E, F, M, W, d, e, f, m, w, cc
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

def collect(info):
    if info:
        print(info)

MAXCLOCK = 50

def run():
    clock = 0
    while W.stat in [SAOK]:
        collect(writebackRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        collect(memoryRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        collect(executeRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        collect(decodeRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        collect(fetchRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))

        collect(writebackUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        collect(memoryUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        collect(executeUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        collect(decodeUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        collect(fetchUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        clock += 1
        if clock == MAXCLOCK:
            break


if __name__ == "__main__":
    os.chdir("C:\\Users\\ichne\\Documents\\Vue-Y86\\backend")
    instrCode = io.StringIO(open("sample.yo", "r").read())
    init(instrCode)
    #mem.show()
    pipe.init()
    run()
