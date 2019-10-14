tuple1 = ('Python', 'C', 'Java')

for i in range(len(tuple1)):
    print(tuple1[i])

print(tuple1)

list1 = [1, 2, 3, 4, 5, 6]
tuple1 = tuple(list1)
print(tuple1)


tuple1 = (1, 2, 3, 4, 5, 6)
tuple1 += (7,)
print(tuple1)
tuple1 += (7, 8)
print(tuple1)

del tuple1
print(tuple1)