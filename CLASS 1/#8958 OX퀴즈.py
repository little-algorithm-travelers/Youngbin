N = int(input())
for i in range(N):
    temp = 0
    answer = 0
    result = input()
    for j in result:
        if j == 'O':
            temp += 1
            answer += temp
        else:
            temp = 0
    print(answer)
