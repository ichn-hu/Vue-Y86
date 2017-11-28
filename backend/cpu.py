"""
CPU implemention, including all the control logics
"""
from const import *
from register import Register

class CPU:
    def __init__(_, mem):
        _.mem = mem
        _.reg = Register()
        _.F_predPC = _.reg[RESP]
        _.f_stat = SAOK
        _.imem_error = 
        _.instr_valid = 
        _.f_pc
        _.f_predPC

        _.D_stat
        _.D_icode
        _.D_ifun
        _.D_rA
        _.D_rB
        _.D_valC
        _.D_valP
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
        _.M_icode
        _.M_Cnd
        _.M_valE
        _.M_valA
        _.M_dstE
        _.M_dstM
        _.m_stat
        _.dmem_error

        _.W_stat
        _.W_icode
        _.W_valE
        _.W_valM
        _.W_dstE
        _.W_dstM

        
    def fetch(_):
        pass
    def decode(_):
        pass
    def excute(_):
        pass
    def memory(_):
        pass
    def writeBack(_):
        pass

if __name__ == "__main__":
