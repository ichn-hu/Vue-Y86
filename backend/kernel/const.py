"""
该文件中定义的所有变量都被认为是常量, 将只作为右值使用.
这些值将出现在pipeline register中. 具体定义参见csapp2e, Figure 4.26 Constant values used in HCL descriptions.
此外, 补充定义IIADDL, ILEAVE, REBP, 以提供对指令iaddl和leave的支持.
"""
IHALT = 0x0   # Code for halt instruction
INOP = 0x1    # Code for nop instruction
IRRMOVL = 0x2  # Code for rrmovl instruction
IIRMOVL = 0x3  # Code for irmovl instruction
IRMMOVL = 0x4  # Code for rmmovl instruction
IMRMOVL = 0x5  # Code for mrmovl instruction
IOPL = 0x6    # Code for integer operation instructions
IJXX = 0x7    # Code for jump instructions
ICALL = 0x8   # Code for call instruction
IRET = 0x9    # Code for ret instruction
IPUSHL = 0xA  # Code for pushl instruction
IPOPL = 0xB   # Code for popl instruction
FNONE = 0x0   # Default function code
REAX = 0x0    # Register ID for %eax
RECX = 0x1    # Register ID for %ecx
REDX = 0x2    # Register ID for %edx
REBX = 0x3    # Register ID for %ebx
RESP = 0x4    # Register ID for %esp
REBP = 0x5    # Register ID for %ebp
RESI = 0x6    # Register ID for %esi
REDI = 0x7    # Register ID for %edi
RNONE = 0xF   # Indicates no register file access



ALUADD = 0x0  # Function for addition operation
SAOK = 0x1    # Status code for normal operation
SADR = 0x2    # Status code for address exception
SINS = 0x3    # Status code for illegal instruction exception
SHLT = 0x4    # Status code for halt
SBUB = 0x5    # Status for bubble
SSTA = 0x6    # Signal for stall

IIADDL = 0xc  # Code for iaddl instruction
ILEAVE = 0xd  # Code for leave instruction

CJMP = 0x0
CJLE = 0x1
CJL = 0x2
CJE = 0x3
CJNE = 0x4
CJGE = 0x5
CJG = 0x6

ZERO = "00000000"
FOUR = "04000000"
NEGFOUR = "fcffffff"
AADD = 0x0
ASUB = 0x1
AAND = 0x2
AXOR = 0x4
VNONE = '--------'

MAXCLOCK = 1000
MEMSIZE = 1 << 12

regName = {
    0: 'EAX',
    1: 'ECX',
    2: 'EDX',
    3: 'EBX',
    4: 'ESP',
    5: 'EBP',
    6: 'ESI',
    7: 'EDI',
    0xf: 'null',
    '0': 'EAX',
    '1': 'ECX',
    '2': 'EDX',
    '3': 'EBX',
    '4': 'ESP',
    '5': 'EBP',
    '6': 'ESI',
    '7': 'EDI',
    'f': 'null',
    'F': 'null'
}

instrName = {
    "00": "halt",
    "10": "nop",    
    "20": "rrmovl",
    "21": "cmovle",
    "22": "cmovl",
    "23": "cmove",
    "24": "cmovne",
    "25": "cmovge",
    "26": "cmovg",
    "30": "irmovl",
    "40": "rmmovl",
    "50": "mrmovl",
    "60": "addl",
    "61": "subl",
    "62": "andl",
    "63": "xorl",
    "70": "jmp",
    "71": "jle",
    "72": "jl",
    "73": "je",
    "74": "jne",
    "75": "jge",
    "76": "jg",
    "80": "call",
    "90": "ret",
    "a0": "pushl",
    "b0": "popl",
    "c0": "iaddl",
    "d0": "leave"
}
