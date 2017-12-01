"""
CPU implemention, including all the control logics
"""


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
    nxt = PipeReg()
    ret = {}
    while cur.W.Stat in [SAOK]:
        if clock == MAXCLOCK:
            break
        writeback(cur, nxt, reg)
        memory(cur, nxt, mem)
        execute(cur, nxt)
        decode(cur, nxt, reg)
        fetch(cur, nxt, mem)
        clock += 1

