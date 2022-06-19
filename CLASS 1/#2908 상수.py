A, B = input().split()
a = int(A[2]) * 100 + int(A[1]) * 10 + int(A[0]) * 1
b = int(B[2]) * 100 + int(B[1]) * 10 + int(B[0]) * 1
if a > b:
    print(a)
else:
    print(b)