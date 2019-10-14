list1 = [[1, 2, 3], [4, 5, 6]]
list2 = [[1, 2], [3, 4], [5, 6]]
list3 = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
print(list1[0][0])
print(list1[0][1])
print(list1[0][2])
print(list1[1][0])
print(list1[1][1])
for i in range(2):
    for k in range(3):
        print(list1[i][k])

print(list1)
print(list1[0])
print(list1[1])

print(len(list1))
print(len(list1[0]))

for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j])
    print()

total = 0
row = 1
for i in range(len(list1[row])):
    total += list1[row][i]
print(total)

total = 0
col = 1
for i in range(len(list1)):
    total += list1[i][col]
print(total)

list1 = ['a', 'b', 'c', '\n', '4', '5', '6']
print(list1)
print(''.join(list1))
print(repr(''.join(list1)))
print(repr(2019))
print('2019')
print('2019'.center(66).rstrip())
print(repr(2019).center(66).rstrip())
print(repr(repr(2019).center(66).rstrip()))
# import random
# row, col = eval(input('input a row and col:'))
# list1 = []
# for i in range(row):
#     list1.append([])
#     for j in range(col):
#         list1[i].append(random.randint(1, 100))
# print(list1)