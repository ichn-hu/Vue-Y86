def split2chunks(s, l):
    return [s[i : i + l] for i in range(0, len(s), l)]