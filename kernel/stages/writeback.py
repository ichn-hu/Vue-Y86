from kernel.const import *
from kernel.misc import swichEndian

def writeback(cur, nxt, reg, ss):
    ss.stat = SAOK if cur.W.stat in [SBUB] else cur.W.stat
    reg.write(cur.W.dstE, cur.W.valE, cur.W.dstM, cur.W.valM)
    op = []
    if cur.W.dstE != RNONE:
        op.append('Write {0} back to {1}'.format(swichEndian(cur.W.valE), regName[cur.W.dstE]))
    if cur.W.dstM != RNONE:
        op.append('Write {0} back to {1}'.format(swichEndian(cur.W.valM), regName[cur.W.dstM]))
    cur.W.__dict__.update(**{
        'operation': op
    })
