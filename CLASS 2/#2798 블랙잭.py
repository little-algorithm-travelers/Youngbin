N, M = map(int, input().split())
card_list = sorted(list(map(int, input().split())))
answer = 0
for i in range(N-2):
    for j in range(N-i-1):
        for k in range(N-i-j-2):
            if card_list[i] + card_list[j+i+1] + card_list[i+j+k+2] > M:
                break
            if answer < card_list[i] + card_list[j+i+1] + card_list[i+j+k+2]:
                answer = card_list[i] + card_list[j+i+1] + card_list[i+j+k+2]
print(answer)

