def split2chunks(s, l):
    return [s[i : i + l] for i in range(0, len(s), l)]


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

if __name__ == "__main__":
    print(swichEndian("bbccddeeff"))