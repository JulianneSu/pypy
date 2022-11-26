n = int(input())
d = set()
for i in range(n):
    s = set(input().split())
    d = d | s
print(*d, sep='\n')