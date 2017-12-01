from stages.execute import aluAdd, aluAnd, aluSub, aluXor

class CC:
    def __init__(self):
        CC.ZF = None
        CC.SF = None
        CC.OF = None

a = "0f0f0f0f"
b = "f0f0f0f0"
c = aluAdd(a, b, True, CC)
print(c, CC.ZF, CC.SF, CC.OF)