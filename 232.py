n = int(input())
a = list(map(int,input().split()))
for i in range(1,len(a)):
    cur = a[i]
    j = i-1
    while j>= 0:
        if a[j] > cur:
            a [j], a[j+1] = a[j+1], a[j]
            j -=1
        else:
            break
print(*a)