n = int(input())
nd = int(input())
for i in range(n - 1):
    x2 = int(input())
    _nod = 0
    while (nd != 0) and (x2 != 0):
        if nd > x2:
            nd = nd % x2
        else:
            x2 = x2 % nd
    nd = x2 + nd

print(nd)

