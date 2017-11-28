class Register:
    def __init__(self):
        self.reg = ["00" * 4] * 8
    def read(self, srcA, srcB):
        srcA = int(srcA)
        srcB = int(srcB)
        valA, valB = None, None
        if srcA != 0xf:
            valA = self.reg[srcA]
        if srcB != 0xf:
            valB = self.reg[srcB]
        return valA, valB
    
    def write(self, dstE, valE, dstM, valM):
        dstE = int(dstE)
        dstM = int(dstM)
        if dstE != 0xf:
            self.reg[dstE] = valE
        if dstM != 0xf:
            self.reg[dstM] = valM

if __name__ == "__main__":
    reg = Register()
    reg.write(0x0, "23332333", 0x1, "12341234")
    reg.write(0xf, "12312312", 0x2, "12312111")
    valA, valB = reg.read(0x1, 0x2)
    print(valA + " 23 " + valB)