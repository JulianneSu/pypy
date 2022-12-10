s = [2, 4, 1, 9, 6, 3]
for i in range(1, len(s)):
    for j in range(i, 0, -1):
        if s[j] < s[j-1]:
            s[j], s[j-1] = s[j-1], s[j]
        else:
            break

print(s)
