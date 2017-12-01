"""
CPU implemention, including all the control logics
"""

import sys

import pipe
from memory import Memory
from misc import split2chunks, swichEndian
from pipe import PipeReg
from register import Register
from const import *
from stages.fetch import fetch
from stages.memory import memory
from stages.decode import decode
from stages.execute  import execute
from stages.writeback import writeback
from stages.control import update

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
        writeback(cur, nxt, reg, ss)
        memory(cur, nxt, mem)
        execute(cur, nxt, cc)
        decode(cur, nxt, reg)
        fetch(cur, nxt, mem)
        #print(nxt.F.predPC)
        update(cur, nxt)
        #sys.exit(str(cur.F.predPC))
        info = {}
        info['F'] = cur.F.__dict__
        info['D'] = cur.D.__dict__
        info['E'] = cur.E.__dict__
        info['M'] = cur.M.__dict__
        info['W'] = cur.W.__dict__
        info['reg'] = reg.info()
        clock += 1
        ret[clock] = info
        
    return ret