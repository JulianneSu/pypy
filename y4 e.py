n = int(input())
m = int(input())
a = set()
b = set()
for i in range(n):
    q = input()
    a.add(q)
for i in range(m):
    q = input()
    b.add(q)
if a & b == set():
    print(len(a | b))
else:
    print('Таких нет')