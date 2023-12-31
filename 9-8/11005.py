import string

ref = '0123456789' + string.ascii_uppercase

n, b = map(int, input().split())

count = 0
while b**count <= n:
    count += 1
    # print("count =", count)

result = ''
for i in range(count-1, -1, -1):
    num = n//(b**i)
    # print("num =", num)
    result += ref[num]
    # print("result =", result)
    n -= num*(b**i)
    # print("n =", n)

print(result)