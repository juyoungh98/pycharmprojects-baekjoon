x = int(input())

row = 1
while x > row:
    x -= row
    row += 1

if row%2 == 0:
    print("%d/%d" %(x, row-x+1))

else:
    print("%d/%d" %(row-x+1, x))