"""
Interface with command line, also as test
"""
from memory import Memory
from cpu import Unit

import re, os

def parse(mem, instr):
    for line in instr:
        line = line[:line.find('|')]
        if len(line) == 0 or line.isspace():
            continue
        try:
            pos = int(re.findall('(0x[0-9]+)', line)[0])
            val = int(re.findall('0x[0-9]+:[ ]*([0-9a-fA-F]+)', line)[0])
            mem.write(pos, val)
        except Exception as e:
            raise Exception("Parse error in %s" % line) from e

            

if __name__ == "__main__":
    os.chdir("C:\\Users\\ichne\\Documents\\Vue-Y86\\backend")
    instr = open("sample.yo", "r").read()
    mem = Memory()
    parse(mem, instr)
    cpu = Unit(mem)