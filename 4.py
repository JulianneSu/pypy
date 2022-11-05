n,k = map(int,input().split())
s = list(map(int,input().split()))
m = list(map(int,input().split()))
s.sort()

for i in m:
    l = 0
    r = len(s)-1
    mid = (l+r)//2
    while i != s[mid]:
        if i > s[mid]:
            l = s[mid]+ 1
        else:
            r = s[mid]-1
    if i == s[mid]:
        print('YES')
    else:
        print('NO')
print(s)