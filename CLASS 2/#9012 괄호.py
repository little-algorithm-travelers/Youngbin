T = int(input())
for _ in range(T):
    string = list(input())
    if len(string) % 2 == 1:
        print('NO')
    else:
        flag = 0
        for _ in range(len(string)//2):
            if string[0] == '(':
                for i in range(1, len(string)):
                    if string[i] == ')':
                        del string[i]
                        del string[0]
                        break
            else:
                flag = 1
                break
        if flag == 1 or len(string) > 1:
            print('NO')
        else:
            print('YES')


