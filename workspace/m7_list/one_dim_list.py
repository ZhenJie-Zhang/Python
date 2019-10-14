list1 = ["Python", "C", "Java", "C++"]
print(list1[0])
print(list1[1])
print(list1[2])

for i in range(len(list1)):
    print(list1[i])

list2 = [45, 67, 87, 34, 22, 90]
total = 0
for i in range(len(list2)):
    total += list2[i]
print(total)

print(sum(list2))

def summary(list1):
    total = 0
    for i in range(len(list1)):
        total += list1[i]
    return total

print(summary(list2))
print(sum(list2))
print(max(list2))
print(min(list2))

print(67 in list1)
print(67 in list2)

list3 = list1 + list2
print(list3)
print(type(list3))
print(list1 * 3)