"""
This file provides the definition of the pipeline registers
of all stage.
"""
from const import *
class cc:
    def __init__(self):
        cc.ZF = 1
        cc.SF = 0
        cc.OF = 0

class F:
    def __init__(self):
        F.predPC = ZERO

class f:
    def __init__(self):
        f.imem_error = False
        f.instr_valid = True
        f.stat = SAOK
        f.pc = ZERO
        f.icode = INOP
        f.ifun = FNONE


class D:
    def __init__(self):
        D.stat = SAOK
        D.icode = INOP
        

class d:
    def __init__(self):
        pass
        

class E:
    def __init__(self):
        E.stat = SAOK
        E.icode = INOP
        

class e:
    def __init__(self):
        e.dstE = RNONE
        e.valE = ZERO

        

class M:
    def __init__(self):
        M.stat = SAOK
        M.icode = INOP
        M.valA = ZERO
        M.valE = ZERO
        M.Cnd = False
        M.dstM = RNONE
        M.dstE = RNONE

        

class m:
    def __init__(self):
        m.valM = ZERO
        m.stat = SAOK
        

class W:
    def __init__(self):
        W.stat = SAOK
        W.dstE = ZERO
        W.dstM = ZERO
        W.valM = ZERO
        W.valE = ZERO

class w:
    def __init__(self):
        W.valM = ZERO

STATUS = ()
Stat = SAOK

def init():
    global STATUS
    STATUS = F(), f(), D(), d(), E(), e(), M(), m(), W(), w()
    global Stat
    Stat = SAOK


if __name__ == "__main__":
    init()
