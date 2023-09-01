import math

letter = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']
grade = [4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0, 'P']
scale = [list(_) for _ in zip(letter, grade)]

score = []
credit = []
for i in range(20):
    course = list(input().split())
    if course[2] == "P":
        pass
    else:
        credit.append(float(course[1]))
        for j in range(len(scale)-1):
            if course[2] in scale[j]:
                score.append(float(course[1])*float(scale[j][1]))

print(sum(score)/math.fsum(credit))