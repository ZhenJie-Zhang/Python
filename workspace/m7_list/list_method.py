list1 = []
list1.append(34)
list1.append(56)
print(list1)
list1.append(68)
print(list1)
list1.insert(1, 15)
val = list1.pop()
print(val)
print(list1)
val = list1.pop(1)
print(val)
print(list1)

list2 = [45, 67, 87, 34, 22, 20, 90, 34, 11, 34]
print(list2.count(34))
list2.remove(34)
print(list2)
print(list2.index(34))
list3 = list2.copy()
list2.sort(reverse=True)
print(list2)
list2.reverse()
print(list2)
print(list3)

import random

list3 = []
for i in range(6):
    list3.append(random.randint(1, 100))
print(list3)