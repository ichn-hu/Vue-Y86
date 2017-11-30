"""
所有的流水线寄存器.
"""
from const import *
class cc:
    def __init__(self):
        cc.ZF = True
        cc.SF = False
        cc.OF = False

class F:
    def __init__(self):
        F.predPC = ZERO                # 预测的PC
        F.stall = False
        F.bubble = False

class f:
    def __init__(self):
        f.imem_error = False
        f.instr_valid = True
        f.stat = SAOK
        f.pc = ZERO                    # 这一步执行的PC
        f.icode = INOP                 # 由mem读入
        f.ifun = FNONE                 # 由mem读入
        f.valP = ZERO                  # 自然下一个PC
        f.valC = ZERO                  # 读入的常量
        f.predPC = ZERO                # 预测的PC, update时传给F.predPC
        f.rA = RNONE                   # 由mem读入
        f.rB = RNONE                   # 同上

class D:
    def __init__(self):
        D.stat = SAOK
        D.icode = INOP
        D.ifun = FNONE
        D.rA = RNONE                   # mem读入
        D.rB = RNONE                   # mem读入
        D.valC = ZERO                  # 同上
        D.valP = ZERO                  # 同上
        D.stall = False
        D.bubble = False
        

class d:
    def __init__(self):
        d.srcA = RNONE
        d.srcB = RNONE
        d.valA = ZERO
        d.valB = ZERO
        d.dstE = RNONE
        d.dstM = RNONE
        

class E:
    def __init__(self):
        E.stat = SAOK
        E.icode = INOP
        E.ifun = FNONE
        E.valA = ZERO
        E.dstE = RNONE
        E.dstM = RNONE
        E.bubble = False
        E.stall = False
        

class e:
    def __init__(self):
        e.dstE = RNONE
        e.valE = ZERO
        e.Cnd = False

        

class M:
    def __init__(self):
        M.stat = SAOK
        M.icode = INOP
        M.valA = ZERO
        M.valE = ZERO
        M.Cnd = False
        M.dstM = RNONE
        M.dstE = RNONE
        M.bubble = False
        M.stall = False

        

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
        w.Stat = SAOK

STATUS = ()

def init():
    global STATUS
    STATUS = F(), f(), D(), d(), E(), e(), M(), m(), W(), w(), cc()


if __name__ == "__main__":
    init()
