n = int(input())
s = list(map(int,input().split()))
x = int(input())
k = 0
for i in range(n):
    if s[i]==x:
        print(i+1)
