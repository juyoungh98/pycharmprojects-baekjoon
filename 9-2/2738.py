N, M = map(int, input().split())
A, B = [], []
# N개의 줄 (행), M개의 원소 (열)

for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for j in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()
