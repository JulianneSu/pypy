sm = 0
n = int(input())
for i in range(n):
    e = input()
    x = int(input())
    s = 0
    while x > 0:
        y = x % 10
        s += y
        x //= 10
    sm = max(sm, s)
    if s == sm:
        em = e
print(em)