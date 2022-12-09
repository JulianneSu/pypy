s = list(map(int, input().split()))
d = dict()
ans = []
for i in s:
    x = bin(i)[2:]
#    print(x)
    zeros = units = digits = 0
    for q in x:
        if q == '0':
            zeros += 1
    units = len(x) - zeros
    digit = len(x)

    d = {'digits': digit, 'units': units, 'zeros': zeros}
    ans.append(d)
print(ans)
