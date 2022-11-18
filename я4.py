n = int(input())
s = 0
for i in range(n):
    x = int(input())
    while x > 0:
        y = x % 10
        s += y
        x //= 10
print(s)