import os
import io
import json, pprint

import kernel.cpu as cpu

if __name__ == "__main__":
    os.chdir("C:\\Users\\ichne\\Documents\\Vue-Y86\\kernel\\test")
    c0 = io.StringIO(open("asum.yo", "r").read())
    c1 = io.StringIO(open("prog1.yo", "r").read())
    c2 = io.StringIO(open("prog2.yo", "r").read())
    c3 = io.StringIO(open("prog3.yo", "r").read())
    c4 = io.StringIO(open("prog4.yo", "r").read())
    c5 = io.StringIO(open("prog5.yo", "r").read())
    c6 = io.StringIO(open("prog6.yo", "r").read())
    c7 = io.StringIO(open("prog7.yo", "r").read())
    c8 = io.StringIO(open("prog8.yo", "r").read())
    c9 = io.StringIO(open("prog9.yo", "r").read())
    ca = io.StringIO(open("prog10.yo", "r").read())
    cb = io.StringIO(open("pushquestion.yo", "r").read())
    cc = io.StringIO(open("pushtest.yo", "r").read())
    cd = io.StringIO(open("ret-hazard.yo", "r").read())
    ce = io.StringIO(open("cjr.yo", "r").read())
    cf = io.StringIO(open("poptest.yo", "r").read())
    cg = io.StringIO(open("asumr.yo", "r").read())
    instrCode = c0
    cpu.init(instrCode)
    res = cpu.run()
    output = pprint.pformat(res, indent=2)
    open('run.txt', 'w').write(json.dumps(res, indent=2))