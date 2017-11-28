import re
import os
from var import mem
import re
def parse(instr):
    for line in instr:
        try:
            pos = int(re.findall('(0x[0-9]+)', line)[0])
            val = int(re.findall('0x[0-9]+:[ ]*([0-9a-fA-F]+)', line)[0])
            mem.write(pos, val)
        except Exception as e:
            raise Exception("Parse error in %s" % line) from e

            