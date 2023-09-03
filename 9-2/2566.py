matrix = []

for i in range(9):
    matrix.append(list(map(int, input().split())))

maxVal = []
maxRow = []
maxCol = []
for j in range(len(matrix)):
    maxVal.append(max(matrix[j]))
    maxRow.append(j+1)
    maxCol.append(matrix[j].index(max(matrix[j])) + 1)

print(max(maxVal))
print(maxRow[maxVal.index(max(maxVal))], maxCol[maxVal.index(max(maxVal))])