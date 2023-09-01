import string

word = list(input())

# 대소문자 구분 없애기
for i in range(len(word)):
    word[i] = word[i].lower()
# upper = string.ascii_uppercase
# lower = string.ascii_lowercase
# for i in range(len(word)):
#     if word[i] in upper:
#         word[i] = lower[upper.index(word[i])]

# 글자별 개수 세기
unique = list(set(word))
count = []
for letter in unique:
    count.append(word.count(letter))

# 조건에 맞춰 출력하기
if count.count(max(count)) > 1:
    print('?')
else:
    print(unique[count.index(max(count))].upper())
#   print(upper[lower.index(unique[count.index(max(count))])])

