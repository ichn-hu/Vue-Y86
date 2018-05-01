"""
CPU implemention, including all the control logics
"""

import sys
import time
import threading
import logging

import kernel.pipe as pip
from kernel.memory import Memory
from kernel.misc import split2chunks, swichEndian
from kernel.pipe import PipeReg
from kernel.register import Register
from kernel.const import *
from kernel.parallel_stages.fetch import fetch
from kernel.parallel_stages.memory import memory
from kernel.parallel_stages.decode import decode
from kernel.parallel_stages.execute  import execute
from kernel.parallel_stages.writeback import writeback
from kernel.parallel_stages.control import update

class ThreadException(Exception):
    pass


reg, mem = None, None

def init(instrCode):
    global reg, mem
    reg = Register()
    mem = Memory()
    mem.load(instrCode)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

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

        W_over = threading.Event()
        M_over = threading.Event()
        E_over = threading.Event()
        D_over = threading.Event()
        F_over = threading.Event()

        W = threading.Thread(name="writeback", target=writeback, args=(cur, nxt, reg, ss, W_over, logging))
        M = threading.Thread(name="memory", target=memory, args=(cur, nxt, mem, W_over, M_over, logging))
        E = threading.Thread(name="execute", target=execute, args=(cur, nxt, cc, M_over, E_over, logging))
        D = threading.Thread(name="decode", target=decode, args=(cur, nxt, reg, E_over, D_over, logging))
        F = threading.Thread(name="fetch", target=fetch, args=(cur, nxt, mem, D_over, F_over, logging))

        logging.debug("W started")
        W.start()
        logging.debug("M started")
        M.start()
        logging.debug("E started")
        E.start()
        logging.debug("D started")
        D.start()
        logging.debug("F started")
        F.start()

        logging.debug("Waiting for F")
        F_over.wait()
        logging.debug("All Over!")


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