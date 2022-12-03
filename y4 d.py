s = list(input().split())
for i in range(len(s) - 1):
    s[i] += ' '
from itertools import accumulate
for val in accumulate(s):
    print(val)