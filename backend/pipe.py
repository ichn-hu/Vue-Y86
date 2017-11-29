"""
This file provides the definition of the pipeline registers
of all stage.
"""
from const import *
class F:
    def __init__(self):
        F.predPC = ZERO
        pass
class f:
    def __init__(self):
        f.imem_error = False
        f.instr_valid = True
        f.stat = SAOK
        f.pc = ZERO


class D:
    def __init__(self):
        pass
        

class d:
    def __init__(self):
        pass
        

class E:
    def __init__(self):
        pass
        

class e:
    def __init__(self):
        pass
        

class M:
    def __init__(self):
        pass
        

class m:
    def __init__(self):
        pass
        

class W:
    def __init__(self):
        pass


class w:
    def __init__(self):
        pass

STATUS = ()

def init():
    global STATUS
    STATUS = F(), f(), D(), d(), E(), e(), M(), m(), W(), w()


if __name__ == "__main__":
    init()


"""
self.mem = mem
        self.reg = Register()
        self.F_predPC = ZERO
        self.f_stat = SAOK
        self.imem_error = False
        self.instr_valid = True
#        self.f_pc
#        self.f_predPC

        self.D_stat = SAOK
        self.D_icode = INOP
        self.D_ifun = FNONE
        self.D_rA = RNONE
        self.D_rB = RNONE
        self.D_valC = ZERO
        self.D_valP = ZERO
        self.d_rvalA
        self.d_srcA
        self.d_srcB

        self.E_stat
        self.E_icode
        self.E_ifun
        self.E_valC
        self.E_valA
        self.E_valB
        self.E_dstE
        self.E_dstM
        self.E_srcA
        self.E_srcB
        self.e_Cnd
        self.e_dstM

        self.M_stat
        self.M_icode = INOP
        self.M_Cnd = False
        self.M_valE = ZERO
        self.M_valA = ZERO
        self.M_dstE = RNONE
        self.M_dstM = RNONE
        self.m_stat
        self.dmem_error

        self.W_stat
        self.W_icode
        self.W_valE
        self.W_valM = ZERO
        self.W_dstE
        self.W_dstM

"""