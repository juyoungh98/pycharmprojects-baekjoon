N, M = map(int, input().split())
basket = list(range(1, N + 1))

for x in range(M):
    i, j = map(int, input().split())
    basket[i - 1:j] = reversed(basket[i - 1:j])

for y in range(len(basket)):
    print(basket[y], end=' ')

# sorted(reverse=True) : 역순 정렬 (내림차순)
# reversed() : 역순