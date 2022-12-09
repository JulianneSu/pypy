n = int(input())
d = dict()
for i in range(n):
    s = list(input().split())
    val = s[0]
    key = []
    for q in range(1, len(s)-1):
        key.join(s[q])
    print(key)
    d[key] = str(val)
kasha = s[-1]
for i in d.keys():
    if kasha in i:
        print(d.get(i), '((')