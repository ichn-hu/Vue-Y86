"""
Interface with command line, also as test
"""
from memory import Memory
from cpu import Unit
import parser.parse

if __name__ == "__main__":
    instr = open("sample.yo", "r").read()
    mem = Memory()
    parser.parse(mem, instr)
    cpu = Unit(mem)