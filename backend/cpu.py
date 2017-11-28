"""
CPU implemention, including all the control logics
"""
from const import *
from register import Register
from misc import split2chunks

class Unit:
    def __init__(_, mem):
        _.mem = mem
        _.reg = Register()
        _.F_predPC = ZERO
        _.f_stat = SAOK
        _.imem_error = False
        _.instr_valid = True
#        _.f_pc
#        _.f_predPC

        _.D_stat = SAOK
        _.D_icode = INOP
        _.D_ifun = FNONE
        _.D_rA = RNONE
        _.D_rB = RNONE
        _.D_valC = ZERO
        _.D_valP = ZERO
        _.d_rvalA
        _.d_srcA
        _.d_srcB

        _.E_stat
        _.E_icode
        _.E_ifun
        _.E_valC
        _.E_valA
        _.E_valB
        _.E_dstE
        _.E_dstM
        _.E_srcA
        _.E_srcB
        _.e_Cnd

        _.M_stat
        _.M_icode = INOP
        _.M_Cnd = False
        _.M_valE = ZERO
        _.M_valA = ZERO
        _.M_dstE = RNONE
        _.M_dstM = RNONE
        _.m_stat
        _.dmem_error

        _.W_stat
        _.W_icode
        _.W_valE
        _.W_valM = ZERO
        _.W_dstE
        _.W_dstM

        
    def fetch(_):
        info = {}
        info["process"] = []


        if _.M_icode == IJXX and not _.M_Cnd:
            f_pc = _.M_valA
        elif _.M_icode == IRET:
            f_pc = _.W_valM
        else:
            f_pc = _.F_predPC
        _.imem_error = False
        try:
            icode, ifun = split2chunks(_.mem.read(f_pc, 1), 1)
        except:
            _.imem_error = True
            ifun = FNONE
            icode = INOP
        _.instr_valid = ifun in [ INOP, IHALT, IRRMOVL, IIRMOVL, IRMMOVL, IMRMOVL, \
                                IOPL, IJXX, ICALL, IRET, IPUSHL, IPOPL]
        if _.imem_error:
            f_stat = SADR
        elif not _.instr_valid:
            _.f_stat = SINS
        elif icode == IHALT:
            _.f_stat = SHLT
        else:
            _.f_stat = SAOK

        need_regid = icode in [IRRMOVL, IRMMOVL, IMRMOVL, IIRMOVL, IPUSHL, IPOPL, IIADDL]
        need_valC = icode in [IIRMOVL, IRMMOVL, IMRMOVL, IJXX, ICALL, IIADDL]
        valP = _.F_predPC + 1 * int(need_regid) + 4 * int(need_valC)
        if need_valC:
            valC = _.mem.read(f_pc + 1 + int(need_regid), 4)
        else:
            valC = None

        if icode in [IJXX, ICALL]:
            f_predPC = valC
        else:
            f_predPC = valP

        if need_regid:
            rA, rB = split2chunks(_.mem.read(f_pc + 1, 1), 1)
        else:
            rA, rB = RNONE, RNONE

        # 应该在下一个Clock来的时候由f_predPC更新, 不过管他呢233
        # programmer visible state 不会有区别的(蜜汁自信
        
        _.F_predPC = f_predPC
        _.D_valC = valC
        _.D_valP = valP
        _.D_rA = rA
        _.D_rB = rB
        _.D_icode = icode
        _.D_ifun = ifun
        _.D_stat = f_stat

        return info
    def decode(_):
        pass
    def excute(_):
        pass
    def memory(_):
        pass
    def writeBack(_):
        pass
