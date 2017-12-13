"""
所有的流水线寄存器. 与reg, mem一同构成programmer visible state
所有的流水线寄存器都有:
1. ins 表示这个寄存器中存的是哪句指令, 为mem中的地址
2. icode
3. ifun
"""
from kernel.const import *

ZF = 'ZF'
SF = 'SF'
OF = 'OF'
ins = 'ins'
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
            ins: VNONE,
            predPC: ZERO,
            bubble: False,
            stall: False,
        })
        self.D = self.Reg(**{
            ins: VNONE,
            stat: SBUB,
            icode: INOP,
            ifun: FNONE,
            rA: RNONE,
            rB: RNONE,
            valC: VNONE,
            valP: VNONE,
            bubble: False,
            stall: False,
        })
        self.E = self.Reg(**{
            ins: VNONE,
            stat: SBUB,
            icode: INOP,
            ifun: FNONE,
            valC: VNONE,
            valA: VNONE,
            valB: VNONE,
            dstE: RNONE,
            dstM: RNONE,
            srcA: RNONE,
            srcB: RNONE,
            bubble: False,
            stall: False,
        })
        self.M = self.Reg(**{
            ins: VNONE,
            stat: SBUB,
            icode: INOP,
            Cnd: False,
            valA: VNONE,
            valE: VNONE,
            dstM: RNONE,
            dstE: RNONE,
            bubble: False,
            stall: False,
        })
        self.W = self.Reg(**{
            ins: VNONE,
            stat: SBUB,
            icode: INOP,            
            dstE: RNONE,
            dstM: RNONE,
            valM: VNONE,
            valE: VNONE,
            bubble: False,
            stall: False,
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
