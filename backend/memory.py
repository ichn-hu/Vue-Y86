from misc import split2chunks

MEMSIZE = 1 << 12

class Memory:
    """
    实现内存模拟, 提供读和写, 本身是个大字符串类似物.
    注意, 在实现中, 所有的字面值(literal)都以字符串的方式存储, 得益于python对字符串
    处理的优秀支持.
    """
    def __init__(self):
        self.mem = ["00"] * MEMSIZE
    def read(self, pos, length):
        if pos < 0 or pos + length > MEMSIZE:
            raise Exception \
            (("Trying to read data from %d to %d"  %  (pos, pos + length)))
        return "".join(self.mem[pos : pos + length])
    def write(self, pos, val):
        if pos < 0 or pos + len(val) > MEMSIZE:
            raise Exception \
            (("Trying to write data from %d to %d"  %  (pos, pos + len(val))))
        self.mem[pos : pos + int(len(val) / 2)] = split2chunks(val, 2)

if __name__ == "__main__":
    t_mem = Memory()
    print(t_mem.read(0, 2))
    t_mem.write(-1, "aabbccddeeff")
    print(t_mem.read(0, 2))