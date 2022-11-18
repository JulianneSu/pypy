x = int(input())
a=[]
s =0
import math
w =int(str(x**0,5))
for i in range(1, w +1):
    if x % i == 0:
        a.append(i)
        s +=i

if s!=x:
    print(0)
else:
    print(*a)
