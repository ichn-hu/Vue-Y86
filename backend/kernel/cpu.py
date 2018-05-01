"""
CPU implemention, including all the control logics
"""

import sys

import kernel.pipe as pip
from kernel.memory import Memory
from kernel.misc import split2chunks, swichEndian
from kernel.pipe import PipeReg
from kernel.register import Register
from kernel.const import *
from kernel.stages.fetch import fetch
from kernel.stages.memory import memory
from kernel.stages.decode import decode
from kernel.stages.execute  import execute
from kernel.stages.writeback import writeback
from kernel.stages.control import update

reg, mem = None, None

def init(instrCode):
    global reg, mem
    reg = Register()
    mem = Memory()
    mem.load(instrCode)
    
def run():
    clock = 0
    cur = PipeReg()
    ret = {}
    class CondCode:
        def __init__(self):
            self.ZF = True
            self.SF = False
            self.OF = False
    class Stat:
        def __init__(self):
            self.stat = SAOK

    cc = CondCode()
    ss = Stat()
    while ss.stat in [SAOK] and clock < MAXCLOCK:
        nxt = PipeReg()
        over = []
        writeback(cur, nxt, reg, ss)
        memory(cur, nxt, mem)
        execute(cur, nxt, cc)
        decode(cur, nxt, reg)
        fetch(cur, nxt, mem)
        info = {}
        info['F'] = cur.F.__dict__
        info['D'] = cur.D.__dict__
        info['E'] = cur.E.__dict__
        info['M'] = cur.M.__dict__
        info['W'] = cur.W.__dict__
        info['reg'] = reg.info()
        info['mem'] = mem.info()
        info['cc'] = {}
        info['cc'].update(cc.__dict__)
        info['control'] = update(cur, nxt)

        ret[clock] = info
        clock += 1
        
    ret['Stat'] = ss.stat
    return ret