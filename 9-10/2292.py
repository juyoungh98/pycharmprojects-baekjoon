n = int(input())

# SOL3 : 정답; 메모리 초과 => 공간복잡도 고려
if n == 1:
    print(n)
else:
    hive = 1
    count = 1
    while hive < n:
        hive += count*6
        count += 1
    print(count)

# SOL1 : 메모리 초과
# hive = [[i]]
# for i in range(n//6):
#     hive.append(hive[i] + 6*(i+1))
    # start = hive[i][-1] + 1
    # hive.append([num for num in range(start, start + (6 * (i + 1)))])
# for j in range(len(hive)):
#     if n in hive[j]:
#         print(j+1)
#         break

# SOL2 : 메모리 초과
# hive = [1]
# for i in range(n//6):
#     hive.append(hive[i] + 6*(i+1))
# for j in range(len(hive)):
#     if n <= hive[j]:
#         print(j+1)
#         break