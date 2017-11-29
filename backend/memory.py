from misc import split2chunks
import re

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
    def load(self, instr):
        for line in instr:
            line = line[:line.find('|')]
            if len(line) == 0 or line.isspace():
                continue
            try:
                pos = int(re.findall('(0x[0-9]+)', line)[0])
                val = int(re.findall('0x[0-9]+:[ ]*([0-9a-fA-F]+)', line)[0])
                self.write(pos, val)
            except Exception as e:
                raise Exception("Parse error in %s" % line) from e

if __name__ == "__main__":
    t_mem = Memory()
    print(t_mem.read(0, 2))
    t_mem.write(-1, "aabbccddeeff")
    print(t_mem.read(0, 2))