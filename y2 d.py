s = []
while True:
    a = input()
    if a == '':
        break
    s.append(a)
for i in range(len(s)):
    q = s[i]
    if q[:4] == '##' or q[(len(q)-3):] == '@@@':
        q.replace('##','',1)
     q[(len(q)-3):] == '##':


