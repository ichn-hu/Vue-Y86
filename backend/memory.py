from stages.misc import split2chunks
import re

MEMSIZE = 1 << 12

def debug(*args):
    print(*args)
    pass

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
            raise Exception(
                ("Trying to read data from %d to %d" % (pos, pos + length)))
        return "".join(self.mem[pos: pos + length])

    def write(self, pos, val):
        if pos < 0 or pos + len(val) > MEMSIZE:
            raise Exception(
                ("Trying to write data from %d to %d" % (pos, pos + len(val))))
        self.mem[pos: pos + len(val) // 2] = split2chunks(val, 2)

    def load(self, instr):
        for line in instr:
            if line.find('|') != -1:
                line = line[:line.find('|')]
            if len(line) == 0 or line.isspace():
                continue
            pos = None
            val = None
            try:
                pos_tags = re.findall('(0x[0-9a-fA-F]+)', line)
                val_tags = re.findall('0x[0-9a-fA-F]+:[ ]*([0-9a-fA-F]+)', line)
                if len(pos_tags) != 0:
                    pos = int(pos_tags[0], 16)
                    if len(val_tags) != 0:
                        val = val_tags[0]
                        debug(pos, val)
                        self.write(pos, val)
            except Exception as e:
                raise Exception("Parse error in %s" % line) from e

    def show(self):
        pLen = MEMSIZE
        while pLen >= 4 and (''.join(self.mem[pLen - 4:pLen])) == "00" * 4:
            pLen -= 4
        for i in range(0, pLen, 4):
            for j in range(0, 4):
                debug(self.mem[i + j], end='\n' if j == 3 else ' ')


if __name__ == "__main__":
    t_mem = Memory()
    print(t_mem.read(0, 2))
    t_mem.write(-1, "aabbccddeeff")
    print(t_mem.read(0, 2))
