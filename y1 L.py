n = int(input())
m = int(input())
x = 0
for i in range(n):
    for i in range(m):
        x += 1
        if x % m == 0:
            print(x, end='')
        else:
            print(x, end=' ')
    print()