from kernel.const import *


def split2chunks(s, l):
    return [s[i: i + l] for i in range(0, len(s), l)]


def int16(v):
    return int(v, 16)


def toInteger(v):
    return int(swichEndian(v), 16)


def swichEndian(s):
    if s.startswith("0x") or s.startswith("0X"):
        s = s[2:]
    if len(s) > 8:
        s = s[-8:]
    s = "0" * (8 - len(s)) + s
    return ''.join(reversed(split2chunks(s, 2)))


def toHex(val):
    """
    Turn int val to string in hex
    """
    digits = []
    tmp = val
    while tmp != 0:
        digits.append(tmp % 2)
        tmp //= 2
    if len(digits) < 32:
        digits = digits + [0] * (32 - len(digits))

    if val >= 0:
        s = hex(val)
        s = s[2:]
        if len(s) > 8:
            s = s[-8:]
        s = "0" * (8 - len(s)) + s
    else:
        val = ~val + 1
        s = hex(val)
    return s


def aluAdd(a, b, c, cc):
    pass


def aluSub(a, b, c, cc):
    pass


def aluAnd(a, b, c, cc):
    pass


def aluXor(a, b, c, cc):
    pass


def d2h(d):
    return "0123456789abcdef"[int(d)]


def disassemble(icode, ifun, rA, rB, valC):
    ins = d2h(icode) + d2h(ifun)
    try:
        ret = instrName[ins]
        if icode in [IRRMOVL, IOPL]:
            ret += ' %s, %s' % (regName[rA], regName[rB])
        elif icode in [IIRMOVL]:
            ret += ' %s, %s' % (swichEndian(valC), regName[rB])
        elif icode in [IRMMOVL]:
            ret += ' %s, %s(%s)' % (regName[rA],
                                    str(toInteger(valC)), regName[rB])
        elif icode in [IMRMOVL]:
            ret += ' %s(%s), %s' % (str(toInteger(valC)),
                                    regName[rB], regName[rA])
        elif icode in [IJXX, ICALL]:
            ret += ' %s' % (swichEndian(valC))
        elif icode in [IPOPL, IPUSHL]:
            ret += ' %s' % (regName[rA])
    except:
            ret = 'Invalid'
    return ret


if __name__ == "__main__":
    print(disassemble(IMRMOVL, 0, 0, 0, 1, 2, '30303333'))
