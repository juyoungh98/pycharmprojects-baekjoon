nums = [['' for _ in range(15)] for _ in range(5)]

words = []
for i in range(len(nums)):
    words.append(list(input()))
    for j in range(len(words[i])):
        nums[i][j] = words[i][j]

for i in range(len(nums[0])):
    for j in range(len(nums)):
        print(nums[j][i], end="" if nums[j][i] != '' else '')