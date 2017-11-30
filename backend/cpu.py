"""
CPU implemention, including all the control logics
"""
import os
import io

import pipe
from memory import Memory
from stages.misc import split2chunks, swichEndian
from pipe import D, E, F, M, W, d, e, f, m, w, cc
from register import Register
from stages.const import *
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


MAXCLOCK = 50

def run():
    clock = 0
    while w.Stat in [SAOK]:
        clock += 1
        if clock > MAXCLOCK:
            break
        info = {
            'W': {},
            'M': {},
            'E': {},
            'D': {},
            'F': {},
            'cyc': clock
        }
        
        info['W'].update(writebackUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        info['M'].update(memoryUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        info['E'].update(executeUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        info['D'].update(decodeUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        info['F'].update(fetchUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))

        info['W'].update(writebackRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        info['M'].update(memoryRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        info['E'].update(executeRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        info['D'].update(decodeRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))
        info['F'].update(fetchRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg))

        info['reg'] = reg.info()
        info['mem'] = mem.info()


if __name__ == "__main__":
    os.chdir("C:\\Users\\ichne\\Documents\\Vue-Y86\\backend\\test")
    c1 = io.StringIO(open("sample.yo", "r").read())
    c2 = io.StringIO(open("c2.yo", "r").read())
    c3 = io.StringIO(open("c3.yo", "r").read())
    c4 = io.StringIO(open("c4.yo", "r").read())
    instrCode = c1
    init(instrCode)
    #mem.show()
    pipe.init()
    run()
