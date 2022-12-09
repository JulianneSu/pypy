n = int(input())
sname = [input() for i in range(n)]
d = dict()
for i in sorted(sname):
    d[i] = 0
for i in sname:
    d[i] += 1
k = 0
for i in d:
    if d.get(i) > 1:
        print(f"{i} - {d.get(i)}")
        k = 1
if k == 0:
    print("Однофамильцев нет")