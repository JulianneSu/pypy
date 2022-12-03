s = list(input().split())
from itertools import enumerate
for i, _s in enumerate(s, 1):
    print(f'{i}' + '.', _s)
print(s)