n = int(input())
k =0
a = list(map(int,input().split()))
for i in range (len(a)):
    f = False
    for j in range (len(a)-1, 0, -1):

        if a[j] < a [j-1]:
            a [j], a [j-1] = a[j-1], a[j]
            f = True

    if not f:
            break
print(a)
