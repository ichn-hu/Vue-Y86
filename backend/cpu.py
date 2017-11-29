"""
CPU implemention, including all the control logics
"""
from const import *
from register import Register
from misc import split2chunks

class Unit:
    def __init__(self, mem):
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

        
    def fetch(self):
        info = {}
        info["process"] = []


        if self.M_icode == IJXX and not self.M_Cnd:
            f_pc = self.M_valA
        elif self.M_icode == IRET:
            f_pc = self.W_valM
        else:
            f_pc = self.F_predPC
        self.imem_error = False
        try:
            icode, ifun = split2chunks(self.mem.read(f_pc, 1), 1)
        except:
            self.imem_error = True
            ifun = FNONE
            icode = INOP
        self.instr_valid = ifun in [ INOP, IHALT, IRRMOVL, IIRMOVL, IRMMOVL, IMRMOVL, \
                                IOPL, IJXX, ICALL, IRET, IPUSHL, IPOPL]
        if self.imem_error:
            f_stat = SADR
        elif not self.instr_valid:
            self.f_stat = SINS
        elif icode == IHALT:
            self.f_stat = SHLT
        else:
            self.f_stat = SAOK

        need_regid = icode in [IRRMOVL, IRMMOVL, IMRMOVL, IIRMOVL, IPUSHL, IPOPL, IIADDL]
        need_valC = icode in [IIRMOVL, IRMMOVL, IMRMOVL, IJXX, ICALL, IIADDL]
        valP = self.F_predPC + 1 * int(need_regid) + 4 * int(need_valC)
        if need_valC:
            valC = self.mem.read(f_pc + 1 + int(need_regid), 4)
        else:
            valC = None

        if icode in [IJXX, ICALL]:
            f_predPC = valC
        else:
            f_predPC = valP

        if need_regid:
            rA, rB = split2chunks(self.mem.read(f_pc + 1, 1), 1)
        else:
            rA, rB = RNONE, RNONE

        # 应该在下一个Clock来的时候由f_predPC更新, 不过管他呢233
        # programmer visible state 不会有区别的(蜜汁自信
        # 执行的时候是倒着来的, WMEDF
        
        self.F_predPC = f_predPC
        self.D_valC = valC
        self.D_valP = valP
        self.D_rA = rA
        self.D_rB = rB
        self.D_icode = icode
        self.D_ifun = ifun
        self.D_stat = f_stat

        return info

    def decode(self):
        info = {}
        info["process"] = []
        if self.D_icode in [IRRMOVL, IRMMOVL, IOPL, IPUSHL]:
            d_srcA = self.D_rA
        elif self.D_icode in [IPOPL, IRET]:
            d_srcA = RESP
        else:
            d_srcA = RNONE
        
        if self.D_icode in [IOPL, IRMMOVL, IMRMOVL]:
            d_srcB = self.D_rB
        elif self.D_icode [IPUSHL, IPOPL, ICALL, IRET]:
            d_srcB = RESP
        else:
            d_srcB = RNONE
        
        if self.D_icode in [IRRMOVL, IIRMOVL, IOPL]:
            d_dstE = self.D_rB
        elif self.D_icode in [IPOPL, IPOPL, ICALL, IRET]:
            d_dstE = RESP
        else:
            d_dstE = RNONE
        
        if self.D_icode in [IMRMOVL, IPOPL]:
            d_dstM = self.D_rB
        else:
            d_dstM = RNONE
        
        d_rvalA, d_rvalB = self.reg.read(d_srcA, d_srcB)

        if self.D_icode in [ICALL, IJXX]:
            d_valA = self.D_valP
        elif d_srcA == self.e_dstE:
            d_valA = self.e_valE
        elif d_srcA == self.M_dstM:
            d_valA = self.m_valM
        elif d_srcA == self.M_dstE:
            d_valA = self.M_valE
        elif d_srcA == self.W_dstM:
            d_valA = self.W_valM
        elif d_srcA == self.W_dstE:
            d_valA = self.W_valE
        else:
            d_valA = d_rvalA

        if d_srcB == self.e_dstE:
            d_valB = self.e_valE
        elif d_srcB == self.M_dstM:
            d_valB = self.m_valM
        elif d_srcB == self.M_dstE:
            d_valB = self.M_valE
        elif d_srcB == self.W_dstM:
            d_valB = self.W_valM
        elif d_srcB == self.W_dstE:
            d_valB = self.W_valE
        else:
            d_valB = d_rvalB
        
        # update pipeline register on Excute

        self.E_stat = self.D_stat
        self.E_icode = self.D_icode
        self.E_ifun = self.D_ifun
        self.E_valC = self.D_valC
        self.E_valA = 
        


        


];


        return info
    def excute(self):
        pass
    def memory(self):
        pass
    def writeBack(self):
        pass
