N = int(input())
for i in range(N):
    R, S = input().split()
    for j in range(len(S)):
        print(S[j]*int(R), end="")
    print()

