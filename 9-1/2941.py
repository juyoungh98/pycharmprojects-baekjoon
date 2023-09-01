cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for i in range(len(cro)):
    if cro[i] in word:
        word = word.replace(cro[i], "0")

print(len(word))