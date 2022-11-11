n = int(input())
a = list(map(int,input().split()))

for i in range (len(a)-1):
    ind = i
    for j in range(i, len(a)):
        if a[i] < a[j]:
            ind = j
        a[i], a[ind] = a[ind], a[i]



print(*a)