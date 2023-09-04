import string

ref = '0123456789' + string.ascii_uppercase

b, n = input().split()

num = 0
for i in range(len(b)):
    num += int(ref.index(b[-(i+1)]))*(int(n)**i)
print(num)