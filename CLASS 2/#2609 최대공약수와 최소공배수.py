a, b = map(int, input().split())
answer = 1
for i in range(2, 10001):
    if i > a or i > b:
        break
    else:
        while True:
            if a % i == 0 and b % i == 0:
                answer *= i
                a /= i
                b /= i
            else:
                break
print(answer)
print(round(answer * a * b))

