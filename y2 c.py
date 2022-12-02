q = int(input())
n = int(input())
s = [input() for i in range(n)]
for i in range(n):
    a = s[i]
    if len(s[i]) > q:
        print(a[0:(q - 3)], '...', sep='')
    else:
        print(s[i])