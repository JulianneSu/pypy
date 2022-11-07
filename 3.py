n = int(input())
k= 1
import random
a = n
s = [i for i in range(1,n+1)]
l = 0
r = (n - 1)
m = (l + r) // 2
while a!= s[m] and l<r:
        k+=1
        if a < s[m]:
            r = m-1
        elif a > s[m]:
            l = m+1
        m = (l + r) // 2



print(k)