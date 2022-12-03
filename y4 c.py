from itertools import count
val, end, h = map(float, input(). split())
for val in count(val, h):
    if val <= end:
        print(round(val, 2))
    else:
        break