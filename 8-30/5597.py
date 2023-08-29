students = list(range(1, 31))
print(students)

for i in range(28):
    submit = int(input())
    if submit in students:
        students.remove(submit)
    print(students)

print(min(students))
print(max(students))