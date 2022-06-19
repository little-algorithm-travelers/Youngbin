total = 1
for i in range(3):
    N = int(input())
    total *= N
for i in range(10):
    print(str(total).count(str(i)))
