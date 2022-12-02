man = int(input())
ovs = int(input())
names = []
answ = 0
    for i in range(man + ovs):
        names.append(input())
    for i in names:
    if names.count(i) == 1:
answ += 1
    if answ > 0:
print(answ)
    else:
print('Таких нет')