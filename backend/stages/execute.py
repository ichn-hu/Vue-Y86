from const import *
from misc import swichEndian, split2chunks, d2h, toInteger

def toBinaryList(val):
    """
    turn unsigned val into a binary list, little endian
    """
    digits = []
    tmp = val
    while tmp != 0:
        digits.append(tmp % 2)
        tmp //= 2
    if len(digits) < 32:
        digits = digits + [0] * (32 - len(digits))
    return digits[0:32]


def toSignedInt(bits):
    """
    turn little endian 2 based string to signed int val
    """
    val = 0
    bas = 1
    for i in range(0, len(bits) - 1):
        val = val + bas * int(bits[i])
        bas = bas * 2
    if bits[-1] == 1:
        val -= bas
    return val


def aluAdd(a, b, c, cc):
    a = toBinaryList(toInteger(a))
    b = toBinaryList(toInteger(b))
    valA = toSignedInt(a)
    valB = toSignedInt(b)
    s = [0] * 33
    for i in range(0, 32):
        s[i] += a[i] + b[i]
        if s[i] > 1:
            s[i + 1] = 1
            s[i] %= 2
    res = toSignedInt(s[0:32])
    if c:
        cc.ZF = True if s[0:32] == [0] * 32 else False
        cc.SF = True if s[31] == 1 else False
        cc.OF = True if (valA > 0 and valB > 0 and res < 0) \
            or (valA < 0 and valB < 0 and res > 0) else False
    s = list(reversed(s[0:32]))
    r = []
    for i in range(0, 32, 4):
        t = 0
        for j in range(0, 4):
            t = t * 2 + s[i + j]
        r.append(d2h(t))
    val = ''.join(r)
    return swichEndian(val)


def aluSub(a, b, c, cc):
    a = toBinaryList(toInteger(a))
    b = toBinaryList(toInteger(b))
    valA = toSignedInt(a)
    valB = toSignedInt(b)
    b = list(map(lambda x: 0 if x == 1 else 1, b))
    b[0] += 1
    s = [0] * 33
    for i in range(0, 32):
        s[i] += a[i] + b[i]
        if s[i] > 1:
            s[i + 1] = 1
            s[i] %= 2

    res = toSignedInt(s[0:32])
    if c:
        cc.ZF = True if s[0:32] == [0] * 32 else False
        cc.SF = True if s[31] == 1 else False
        cc.OF = True if (valA > 0 and valB < 0 and res < 0) \
            or (valA > 0 and valB < 0 and res < 0) else False
    s = list(reversed(s[0:32]))
    r = []
    for i in range(0, 32, 4):
        t = 0
        for j in range(0, 4):
            t = t * 2 + s[i + j]
        r.append(d2h(t))
    val = ''.join(r)
    return swichEndian(val)


def aluAnd(a, b, c, cc):
    a = toBinaryList(toInteger(a))
    b = toBinaryList(toInteger(b))
    s = [0] * 32
    for i in range(0, 32):
        s[i] = a[i] & b[i]
    if c:
        cc.ZF = True if s[0:32] == [0] * 32 else False
        cc.SF = True if s[31] == 1 else False
        cc.OF = False
    s = list(reversed(s[0:32]))
    r = []
    for i in range(0, 32, 4):
        t = 0
        for j in range(0, 4):
            t = t * 2 + s[i + j]
        r.append(d2h(t))
    val = ''.join(r)
    return swichEndian(val)


def aluXor(a, b, c, cc):
    a = toBinaryList(toInteger(a))
    b = toBinaryList(toInteger(b))
    s = [0] * 32
    for i in range(0, 32):
        s[i] = a[i] ^ b[i]
    if c:
        cc.ZF = True if s[0:32] == [0] * 32 else False
        cc.SF = True if s[31] == 1 else False
        cc.OF = False
    s = list(reversed(s[0:32]))
    r = []
    for i in range(0, 32, 4):
        t = 0
        for j in range(0, 4):
            t = t * 2 + s[i + j]
        r.append(d2h(t))
    val = ''.join(r)
    return swichEndian(val)


def execute(cur, nxt, cc):

    aluA = ZERO
    if cur.E.icode in [IRRMOVL, IOPL]:
        aluA = cur.E.valA
    elif cur.E.icode in [IIRMOVL, IRMMOVL, IMRMOVL]:
        aluA = cur.E.valC
    elif cur.E.icode in [ICALL, IPUSHL]:
        aluA = NEGFOUR
    elif cur.E.icode in [IRET, IPOPL]:
        aluA = FOUR

    aluB = ZERO
    if cur.E.icode in [IRMMOVL, IMRMOVL, IOPL, ICALL,
                       IPUSHL, IRET, IPOPL]:
        aluB = cur.E.valB

    if cur.E.icode in [IOPL]:
        aluFun = int(cur.E.ifun)
    else:
        aluFun = AADD

    set_cc = True if cur.E.icode in [IOPL] and \
        nxt.W.stat not in [SADR, SINS, SHLT] and \
        cur.W.stat not in [SADR, SINS, SHLT] else False

    if aluFun == AADD:
        valE = aluAdd(aluA, aluB, set_cc, cc)
    elif aluFun == ASUB:
        valE = aluSub(aluB, aluA, set_cc, cc)
    elif aluFun == AAND:
        valE = aluAnd(aluA, aluB, set_cc, cc)
    else:
        valE = aluXor(aluA, aluB, set_cc, cc)

    Cnd = False
    if cur.E.icode in [IJXX, IRRMOVL]:
        if cur.E.ifun in [CJMP]:
            Cnd = True
        elif cur.E.ifun in [CJLE] and ((cc.SF ^ cc.OF) | cc.ZF):
            Cnd = True
        elif cur.E.ifun in [CJL] and (cc.SF ^ cc.OF):
            Cnd = True
        elif cur.E.ifun in [CJE] and cc.ZF:
            Cnd = True
        elif cur.E.ifun in [CJNE] and not cc.ZF:
            Cnd = True
        elif cur.E.ifun in [CJGE] and not (cc.SF ^ cc.OF):
            Cnd = True
        elif cur.E.ifun in [CJG] and not ((cc.SF ^ cc.OF) | cc.ZF):
            Cnd = True

    nxt.M = cur.Reg(**{
        'stat': cur.E.stat,
        'icode': cur.E.icode,
        'Cnd': Cnd,
        'valE': valE,
        'valA': cur.E.valA,
        'dstM': cur.E.dstM,
        'dstE': RNONE if cur.E.icode in [IRRMOVL] and not Cnd else cur.E.dstE,
        'ins': cur.E.ins
    })


if __name__ == "__main__":
    class cc:
        pass
    a = "ffffffff"
    b = "ffffffff"
    print(aluSub(a, b, True, cc))
    print(cc.ZF, cc.SF, cc.OF)
    print(a, b)
