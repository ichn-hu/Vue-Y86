from const import *
from .misc import swichEndian, split2chunks, d2h


def executeUpdate(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):

    E.stall = False
    E.bubble = True if (E.icode in [IJXX] and not e.Cnd) \
        or (E.icode in [IMRMOVL, IPOPL] and E.dstM in [d.srcA, d.srcB]) \
        else False

    if not E.stall and not E.bubble:
        E.stat = D.stat
        E.icode = D.icode
        E.ifun = D.ifun
        E.valC = D.valC
        E.srcA = d.srcA
        E.srcB = d.srcB
        E.valA = d.valA
        E.valB = d.valB
        E.dstE = d.dstE
        E.dstM = d.dstM
    
    if E.bubble:
        E.stat = SBUB
        E.icode = INOP
        E.ifun = FNONE
        E.valC = ZERO
        E.srcA = RNONE
        E.srcB = RNONE
        E.valA = ZERO
        E.valB = ZERO
        E.dstE = RNONE
        E.dstM = RNONE

    ret = {
        'stall': E.stall,
        'bubble': E.bubble,
        'stat': E.stat,
        'icode': E.icode,
        'ifun': E.ifun,
        'valC': E.valC,
        'srcA': E.srcA,
        'srcB': E.srcB,
        'valA': E.valA,
        'valB': E.valB,
        'dstE': E.dstE,
        'dstM': E.dstM
    }
    return ret


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
    a = swichEndian(a)
    b = swichEndian(b)
    a = toBinaryList(int(a, 16))
    b = toBinaryList(int(b, 16))
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
    a = swichEndian(a)
    b = swichEndian(b)
    a = toBinaryList(int(a, 16))
    b = toBinaryList(int(b, 16))
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
        cc.OF = True if (valA < 0 and valB > 0 and res > 0) \
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
    a = swichEndian(a)
    b = swichEndian(b)
    a = toBinaryList(int(a, 16))
    b = toBinaryList(int(b, 16))
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
    a = swichEndian(a)
    b = swichEndian(b)
    a = toBinaryList(int(a, 16))
    b = toBinaryList(int(b, 16))
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


def executeRun(D, E, F, M, W, d, e, f, m, w, cc, mem, reg):

    if E.icode in [IRRMOVL, IOPL, ILEAVE]:
        e.valA = E.valA
    elif E.icode in [IIRMOVL, IRMMOVL, IMRMOVL, IIADDL]:
        e.valA = E.valC
    elif E.icode in [ICALL, IPUSHL]:
        e.valA = NEGFOUR
    elif E.icode in [IRET, IPOPL]:
        e.valA = FOUR
    else:
        e.valA = ZERO

    if E.icode in [IRMMOVL, IMRMOVL, IOPL, ICALL,
                   IPUSHL, IRET, IPOPL, IIADDL]:
        e.valB = E.valB
    elif E.icode in [ILEAVE]:
        e.valB = FOUR
    else:
        e.valB = ZERO

    if E.icode in [IOPL]:
        e.aluFun = int(E.ifun)
    else:
        e.aluFun = AADD

    e.set_cc = E.icode in [IOPL, IIADDL] and \
        m.stat not in [SADR, SINS, SHLT] and \
        W.stat not in [SADR, SINS, SHLT]

    if e.aluFun == AADD:
        e.valE = aluAdd(e.valA, e.valB, e.set_cc, cc)
    elif e.aluFun == ASUB:
        e.valE = aluSub(e.valA, e.valB, e.set_cc, cc)
    elif e.aluFun == AAND:
        e.valE = aluAnd(e.valA, e.valB, e.set_cc, cc)
    else:
        e.valE = aluXor(e.valA, e.valB, e.set_cc, cc)

    e.Cnd = False
    if E.icode == IJXX or E.icode == IRRMOVL:
        if E.ifun in [CJMP]:
            e.Cnd = True
        elif E.ifun in [CJLE] and ((cc.SF ^ cc.OF) | cc.ZF):
            e.Cnd = True
        elif E.ifun in [CJL] and (cc.SF ^ cc.OF):
            e.Cnd = True
        elif E.ifun in [CJE] and cc.ZF:
            print(e.valA, e.valB, e.valE)
            e.Cnd = True
        elif E.ifun in [CJNE] and not cc.ZF:
            e.Cnd = True
        elif E.ifun in [CJGE] and not (cc.SF ^ cc.OF):
            e.Cnd = True
        elif E.ifun in [CJG] and not ((cc.SF ^ cc.OF) | cc.ZF):
            e.Cnd = True

    e.dstE = RNONE if E.icode in [IRRMOVL] and not e.Cnd else E.dstE

    ret = {
        '_valA': e.valA,
        '_valB': e.valB,
        '_aluFun': e.aluFun,
        '_set_cc': e.set_cc,
        '_valE': e.valE,
        '_Cnd': e.Cnd,
        '_dstE': e.dstE
    }
    return ret



if __name__ == "__main__":
    class cc:
        pass
    print(aluAnd("01000000", "01000000", True, cc))
    print(cc.ZF, cc.SF, cc.OF)
    print(aluXor("01000000", "0f000000", True, cc))
    print(cc.ZF, cc.SF, cc.OF)
    print(aluXor("ffffff7f", "ffffffff", True, cc))
    print(cc.ZF, cc.SF, cc.OF)
