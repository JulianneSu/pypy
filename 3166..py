
s=list(map(int,input().split()))
s0 = s [len(s)-1]
for i in range(len(s)-1, 0, -1):
    s[i]= s[i-1]
s[0] = s0
print(*s)