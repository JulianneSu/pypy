n = int(input())
k = 1
s = 0
dk = 1
while s != n:
    for j in range(k):
        if s >= n:
            break
        s += 1
        print(s, end=' ')
    print()
    k += 1



