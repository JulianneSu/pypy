a =0
x = 123
y = 0
while x > 0:
    y = x%10
    a = a*10 +y

    x //= 10
print(a)