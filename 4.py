n,k = map(int,input().split())
s = list(map(int,input().split()))
m = list(map(int,input().split()))
s.sort()

for i in m:
    l = 0
    r = len(s)-1
    mid = (l+r)//2
    for q in s:
        if r < l:
            break
        if i > s[mid]:
            l = s[mid]+ 1
        else:
            r = s[mid]-1
        mid = (l + r) // 2
        if r < l:
            break
        if i == s[mid]:
            print('YES')

    if i != s[mid]:
        print('NO')
