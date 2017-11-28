"""
该文件中定义的所有变量都被认为是常量, 将只作为右值使用.
这些值将出现在pipeline register中. 具体定义参见csapp2e, Figure 4.26 Constant values used in HCL descriptions.
此外, 补充定义IIADDL, ILEAVE, REBP, 以提供对指令iaddl和leave的支持.
"""
INOP = 0x0    # Code for nop instruction
IHALT = 0x1   # Code for halt instruction
IRRMOVL = 0x2 # Code for rrmovl instruction
IIRMOVL = 0x3 # Code for irmovl instruction
IRMMOVL = 0x4 # Code for rmmovl instruction
IMRMOVL = 0x5 # Code for mrmovl instruction
IOPL = 0x6    # Code for integer operation instructions
IJXX = 0x7    # Code for jump instructions
ICALL = 0x8   # Code for call instruction
IRET = 0x9    # Code for ret instruction
IPUSHL = 0xA  # Code for pushl instruction
IPOPL = 0xB   # Code for popl instruction
FNONE = 0x0   # Default function code
RESP = 0x4    # Register ID for %esp
RNONE = 0xF   # Indicates no register file access
ALUADD = 0x0  # Function for addition operation
SAOK = 0x1    # Status code for normal operation
SADR = 0x2    # Status code for address exception
SINS = 0x3    # Status code for illegal instruction exception
SHLT = 0x4    # Status code for halt


REBP = 0x5    # Register ID for %ebp
IIADDL = 0xc  # Code for iaddl instruction
ILEAVE = 0xd  # Code for leave instruction

BUB = 0x1     # Signal for bubble
STA = 0x2     # Signal for stall