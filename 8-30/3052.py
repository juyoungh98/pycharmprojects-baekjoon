nums = list()
for i in range(10):
    num = (int(input()))%42
    nums.append(num)

nums = set(nums)

print(len(nums))