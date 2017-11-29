def split2chunks(s, l):
    return [s[i : i + l] for i in range(0, len(s), l)]

def swichEndien(s):
    if s.startswith("0x") or s.startswith("0X"):
        s = s[2:]
    s = "0" * (8 - len(s)) + s
    return ''.join(reversed(split2chunks(s, 2)))

def d2h(d):
    return "0123456789abcdef"[int(d)]

if __name__ == "__main__":
    print(swichEndien("bbccdd"))