"""
所有的流水线寄存器.
"""
from const import *

ZF = 'ZF'
SF = 'SF'
OF = 'OF'
predPC = 'predPC'
stall = 'stall'
bubble = 'bubble'
stat = 'stat'
Stat = 'Stat'
icode = 'icode'
ifun = 'ifun'
rA = 'rA'
rB = 'rB'
valA = 'valA'
valB = 'valB'
valC = 'valC'
valP = 'valP'
valM = 'valM'
valE = 'valE'
srcA = 'srcA'
srcB = 'srcB'
dstA = 'dstA'
dstB = 'dstB'
dstE = 'dstE'
dstM = 'dstM'
Cnd = 'Cnd'

class PipeReg:
    class Reg:
        def __init__(self, **entries):
            self.__dict__.update(entries)
    def __init__(self):
        self.F = self.Reg(**{
            predPC: ZERO
        })
        self.D = self.Reg(**{
            stat: SBUB,
            icode: INOP,
            ifun: FNONE,
            rA: RNONE,
            rB: RNONE,
            valC: ZERO,
            valP: ZERO,
            'ins': '---'
        })
        self.E = self.Reg(**{
            stat: SBUB,
            icode: INOP,
            ifun: FNONE,
            valC: ZERO,
            valA: ZERO,
            valB: ZERO,
            dstE: RNONE,
            dstM: RNONE,
            srcA: RNONE,
            srcB: RNONE,
            'ins': '---'
        })
        self.M = self.Reg(**{
            stat: SBUB,
            icode: INOP,
            valA: ZERO,
            valE: ZERO,
            Cnd: False,
            dstM: RNONE,
            dstE: RNONE,
            'ins': '---'
        })
        self.W = self.Reg(**{
            icode: INOP,
            stat: SBUB,
            dstE: ZERO,
            dstM: ZERO,
            valM: ZERO,
            valE: ZERO,
            'ins': '---'
        })

        

class PipeReg2:
    class CondCode:
        def __init__(self):
            self.ZF = True
            self.SF = False
            self.OF = False
    class Fetch:
        def __init__(self):
            self.predPC = ZERO
            self.stall = False
            self.bubble = False
    class Decode:
        def __init__(self):
            self.stat = SBUB
            self.icode = INOP
            self.ifun = FNONE
            self.rA = RNONE
            self.rB = RNONE
            self.valC = ZERO
            self.valP = ZERO
            self.stall = False
            self.bubble = False
    class Execute:
        def __init__(self):
            self.stat = SBUB
            self.icode = INOP
            self.ifun = FNONE
            self.valC = ZERO
            self.valA = ZERO
            self.valB = ZERO
            self.dstE = RNONE
            self.dstM = RNONE
            self.srcA = RNONE
            self.srcB = RNONE
            self.bubble = False
            self.stall = False
    class Memory:
        def __init__(self):
            self.stat = SBUB
            self.icode = INOP
            self.valA = ZERO
            self.valE = ZERO
            self.Cnd = False
            self.dstM = RNONE
            self.dstE = RNONE
            self.bubble = False
            self.stall = False
    class Writeback:
        def __init__(self):
            self.icode = INOP
            self.stat = SBUB
            self.dstE = ZERO
            self.dstM = ZERO
            self.valM = ZERO
            self.valE = ZERO
            self.Stat = SAOK
            self.bubble = False
            self.stall = False
    def __init__(self):
        self.W = self.Writeback()
        self.M = self.Memory()
        self.E = self.Execute()
        self.D = self.Decode()
        self.F = self.Fetch()
