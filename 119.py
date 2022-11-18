x = int(input())
k =0
for i in range (1,x+1):
    a =0
    j = i
    while i > 0:
        y = i%10
        a = a*10 +y
        i //= 10
    if a == j:
        k +=1
print(k)
