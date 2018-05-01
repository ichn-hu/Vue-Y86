from kernel.const import *


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

    status = {
        'F_stall': F_stall,
        'D_stall': D_stall,
        'D_bubble': D_bubble,
        'E_bubble': E_bubble,
        'M_bubble': M_bubble,
        'W_stall': W_stall
    }
    #print(status)

    if F_stall:
        nxt.F.__dict__.update(**cur.F.__dict__)
        nxt.F.__dict__.update(**{'stall': True})
    if D_stall:
        nxt.D.__dict__.update(**cur.D.__dict__)
        nxt.D.__dict__.update(**{'stall': True})
    if W_stall:
        nxt.W.__dict__.update(**cur.W.__dict__)
        nxt.W.__dict__.update(**{'stall': True})
    if D_bubble:
        nxt.D.__dict__.update(**{
            'stat': SBUB,
            'icode': INOP,
            'ifun': FNONE,
            'bubble': True
        })
    if E_bubble:
        nxt.E.__dict__.update(**{
            'stat': SBUB,
            'icode': INOP,
            'ifun': FNONE,
            'dstE': RNONE,
            'dstM': RNONE,
            'srcA': RNONE,
            'srcB': RNONE,
            'bubble': True
        })
    if M_bubble:
        nxt.M.__dict__.update(**{
            'stat': SBUB,
            'icode': INOP,
            'Cnd': False,
            'dstM': RNONE,
            'dstE': RNONE,
            'bubble': True
        })
    cur.F = nxt.F
    cur.D = nxt.D
    cur.E = nxt.E
    cur.M = nxt.M
    cur.W = nxt.W
    return status