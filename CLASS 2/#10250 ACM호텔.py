T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    answer = ""
    if ((N % H) == 0):
        answer += str(H)
        if (N // H) < 10:
            answer += '0'
            answer += str((N // H))
        else:
            answer += str((N // H))
        print(answer)
    else:
        answer += str(N % H)
        if (N // H) + 1 < 10:
            answer += '0'
            answer += str((N // H) + 1)
        else:
            answer += str((N // H) + 1)
        print(answer)


