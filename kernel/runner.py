import io
import kernel.cpu as cpu

def runInstrCode(strCode):
    cpu.init(io.StringIO(strCode))
    return cpu.run()
