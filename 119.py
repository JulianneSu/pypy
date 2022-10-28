x = int(input())

a = []
for i in range(1,x):
    for q in str(x):
        y = x % 10
        a.append(y)
        x //= 10

print(a)
