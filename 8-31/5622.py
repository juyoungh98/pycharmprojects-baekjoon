dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()

total = 0
for i in range(len(S)):
    for j in range(len(dial)):
    # for j in dial:
        if S[i] in dial[j]:
        # if S[i] in j:
            total += dial.index(dial[j]) + 3

print(total)

# import string
# S = list(input())
# upperCase = list(string.ascii_uppercase)
# dur = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10]
# total = 0
# for i in range(len(S)):
#     total += dur[upperCase.index(S[i])]
# print(total)
