x = int(input())
for i in range(1, x + 1):
    for j in range(1, x + 1):
        print(i * j, end=" ")
    print(sep="n/")
