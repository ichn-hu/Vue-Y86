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
    if val >= 0:
        s = hex(val)
        s = s[2:]
        if len(s) > 8:
            s = s[-8:]
        s = "0" * (8 - len(s)) + s
    else:
        pass
    return s



def d2h(d):
    return "0123456789abcdef"[int(d)]

if __name__ == "__main__":
    print(swichEndian("bbccddeeff"))