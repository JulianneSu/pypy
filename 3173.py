s = list(map(int,input().split()))
k,km = 0,0
for i in s:
    for q in s:
        if i == q:
            k+=1
 #   km = max(km,k)
    if km<k:
        km = k
        p = i
    k = 0
print(p)
