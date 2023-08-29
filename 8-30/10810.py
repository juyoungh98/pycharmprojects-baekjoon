N, M = map(int, input().split())
basket = [0 for _ in range(N)]

for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i-1, j):
        basket[y] = k

for z in range(len(basket)):
  print(basket[z], end=' ')