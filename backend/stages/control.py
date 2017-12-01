from const import *


def update(cur, nxt):
    F_stall = True if (cur.E.icode in [IMRMOVL, IPOPL]
                       and cur.E.dstM in [nxt.E.srcA, nxt.E.srcB]) \
        or IRET in [cur.D.icode, cur.E.icode, cur.M.icode] else False
    D_stall = True if cur.E.icode in [IMRMOVL, IPOPL] \
        and cur.E.dstM in [nxt.E.srcA, nxt.E.srcB] else False
    D_bubble = True if (cur.E.icode in [IJXX] and not nxt.M.Cnd) \
        or (not D_stall and IRET in [cur.D.icode, cur.E.icode, cur.M.icode]) \
        else False
    E_bubble = True if (cur.E.icode in [IJXX] and not nxt.M.Cnd) \
        or (cur.E.icode in [IMRMOVL, IPOPL] and cur.E.dstM in [nxt.E.srcA, nxt.E.srcB]) \
        else False
    M_bubble = True if nxt.W.stat in [SADR, SINS, SHLT] \
        or cur.W.stat in [SADR, SINS, SHLT] else False
    W_stall = True if cur.W.stat in [SADR, SINS, SHLT] else False

    if F_stall:
        nxt.F = cur.F
    if D_stall:
        nxt.D = cur.D
    if W_stall:
        nxt.W = cur.W
    if D_bubble:
        nxt.D = cur.Reg(**{
            'stat': SBUB,
            'icode': INOP,
            'ifun': FNONE,
            'rA': RNONE,
            'rB': RNONE,
            'valC': ZERO,
            'valP': ZERO,
        })
    if E_bubble:
        nxt.E = cur.Reg(**{
            'stat': SBUB,
            'icode': INOP,
            'ifun': FNONE,
            'valC': ZERO,
            'valA': ZERO,
            'valB': ZERO,
            'dstE': RNONE,
            'dstM': RNONE,
            'srcA': RNONE,
            'srcB': RNONE,
        })
    if M_bubble:
        nxt.M = cur.Reg(**{
            'stat': SBUB,
            'icode': INOP,
            'valA': ZERO,
            'valE': ZERO,
            'Cnd': False,
            'dstM': RNONE,
            'dstE': RNONE,
        })
    cur = nxt
