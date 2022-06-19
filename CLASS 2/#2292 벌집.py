N = int(input())
if N == 1:
    print(1)
else:
    end = 1
    answer = 1
    temp = 1
    while True:
        temp += 1
        if N <= 1 + answer * 6:
            break
        else:
            answer += temp
            end += 1
    print(end + 1)

