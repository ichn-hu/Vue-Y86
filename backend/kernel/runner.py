import io
import kernel.cpu_parallel as cpu

def runInstrCode(strCode):
    cpu.init(io.StringIO(strCode))
    return cpu.run()
