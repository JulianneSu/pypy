x = int(input())
k = 0
s = 0
for i in range(x + 1):
    print(i, sep=' ')

    if k == s:
        print(sep='n/')
        s = 0
    k += 1
    s += 1