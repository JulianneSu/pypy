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
k = 0
for i in range(n):
    k += 1
    if k % 2 != 0:
        print(*s[i])
    else:
        _s = s[i]
        print(*_s[::-1])