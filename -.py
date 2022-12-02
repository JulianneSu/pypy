def nod(nd, x2):
    _nod = 0
    if (nd != 0) and (x2 != 0):
        if nd > x2:
            nd = nd % x2
        else:
            x2 = x2 % nd
    else:
        _nod = nd + x2
    return _nod
print(nod(9, 3))