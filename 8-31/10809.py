import string

S = input()
lowerCase = list(string.ascii_lowercase)
for i in range(len(lowerCase)):
    # index()
    # if lowerCase[i] in S:
    #     lowerCase[i] = S.index(lowerCase[i])
    # else:
    #     lowerCase[i] = -1

    # find()
    lowerCase[i] = S.find(lowerCase[i])

for j in range(len(lowerCase)):
    print(lowerCase[j], end=' ')