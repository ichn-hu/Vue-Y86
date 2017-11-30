import os
import io
import json

import cpu
if __name__ == "__main__":
    os.chdir("C:\\Users\\ichne\\Documents\\Vue-Y86\\backend\\test")
    c1 = io.StringIO(open("sample.yo", "r").read())
    c2 = io.StringIO(open("c2.yo", "r").read())
    c3 = io.StringIO(open("c3.yo", "r").read())
    c4 = io.StringIO(open("c4.yo", "r").read())
    instrCode = c1
    cpu.init(instrCode)
    #mem.show()
    cpu.pipe.init()
    res = cpu.run()
    open('run.txt', 'w').write(json.dumps(res, indent=2))