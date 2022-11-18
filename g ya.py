n = int(input())
k = 3
a = 1
for i in range(n):
    for j in range(k, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {a}!!!')
    k += 1
    a += 1
