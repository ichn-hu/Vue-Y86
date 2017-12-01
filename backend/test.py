from pipe import PipeReg

if __name__ == "__main__":
    a = PipeReg()
    print(a.D.stat)
    b = a.Reg(**{'a': a})
    print(b.a.D.stat)