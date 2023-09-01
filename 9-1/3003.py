pieces = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

for i in range(len(pieces)):
    chess[i] -= pieces[i]

for j in range(len(chess)):
    print(chess[j], end=' ')