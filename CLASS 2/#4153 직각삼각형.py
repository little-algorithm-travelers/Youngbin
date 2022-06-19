while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break
    else:
        max_num = max(numbers)
        numbers.remove(max_num)
        if numbers[0] ** 2 + numbers[1] ** 2 == max_num ** 2:
            print('right')
        else:
            print('wrong')