from const import *


def writeback(cur, nxt, reg, ss):
    ss.stat = SAOK if cur.W.stat in [SBUB] else cur.W.stat
    # TODO: whether the if need to be removed?
    # if not W.bubble and not W.stall:
    if cur.W.icode in [IRMMOVL]:
        return
    else:
        reg.write(cur.W.dstE, cur.W.valE, cur.W.dstM, cur.W.valM)