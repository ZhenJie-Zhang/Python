list1 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

print(list1)

for i in range(len(list1)):
    for j in range(len(list1[i])):
        for k in range(len(list1[i][j])):
            print(list1[i][j][k], end='\t')
        print()
    print()

total = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        for k in range(len(list1[i][j])):
            total += list1[i][j][k]
print(total)

import random
row, col, layer = 2, 3, 3
list1 = []
for i in range(row):
    list1.append([])
    for j in range(col):
        list1[i].append([])
        for k in range(layer):
            list1[i][j].append(random.randint(1, 100))
print(list1)