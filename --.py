nd, x2 = 2, 42
def nod(nd, x2):
    _nod = 0
    while (nd != 0) and (x2 != 0):
        if nd > x2:
            nd = nd % x2
        else:
            x2 = x2 % nd
    return x2 + nd
print(nod(nd, x2))