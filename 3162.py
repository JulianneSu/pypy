s = list(map(int,input().split()))
k = 0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        k+=1

if k != 0:
    k += 1
print(k)