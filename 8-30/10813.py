N, M = map(int, input().split())
basket = list(range(1, N+1))

for x in range(M):
    i ,j = map(int, input().split())
    k = basket[i - 1]
    basket[i - 1] = basket[j - 1]
    basket[j - 1] = k

for y in range(len(basket)):
    print(basket[y], end=' ')