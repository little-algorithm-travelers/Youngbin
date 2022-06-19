while True:
    numbers = list(input())
    if numbers[0] == '0':
        break
    else:
        if len(numbers) == 1:
            print('yes')
        else:
            flag = 0
            for i in range(len(numbers)//2):
                if numbers[i] != numbers[len(numbers) - i - 1]:
                    flag = 1
                    break
            if flag == 0:
                print('yes')
            else:
                print('no')


