n = int(input())
s, f = 0, 0
x = 0
for i in range(n):
    while x != 'ВСЁ':
        x = input()
        if x == 'зайка':
            f = 1
    if f == 1:
        s +=1
    f = 0
    x = 0
print(s)