n = int(input())
m = int(input())
s = []
c = 0
for i in range(n):
    _s = []
    for q in range(m):
        c += 1
        _s.append(c)
    s.append(_s)
for i in range(1, n + 1):
    for j in range(m):
        print(i, end=' ')
        i += n
    print()

