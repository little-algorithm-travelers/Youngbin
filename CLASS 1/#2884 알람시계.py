a, b = map(int, input().split())
if b >= 45:
    print(a, b - 45)
else:
    b = 60 - (45 - b)
    if a == 0:
        a = 23
        print(a, b)
    else:
        a -= 1
        print(a, b)