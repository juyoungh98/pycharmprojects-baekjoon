t = int(input())
usc = [25,10,5,1]
for i in range(t):
    c = int(input())
    change = []
    for coin in usc:
        change.append(c//coin)
        c -= coin*(c//coin)
    for j in range(len(change)):
        print(change[j], end=" ")