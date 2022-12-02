n = int(input())
d = dict()
for i in range(n):
    s = list(input().split())
    key = s[1]
    val = s[2:len(s)]
    d[key] = val
print(d.items)