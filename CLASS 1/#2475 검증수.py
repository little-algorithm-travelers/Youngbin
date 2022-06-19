numbers = list(map(int, input().split()))
#print(numbers)
total = 0
for i in range(len(numbers)):
    total += numbers[i] ** 2
print(total % 10)