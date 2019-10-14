tuple1 = (1,2,3,4,5,6,3,1)
set1 = set(tuple1)
print(set1)

set1.add(6)
print(set1)
set1.remove(4)
print(set1)

set1 = {1,2,3,5,8}
set2 = {1,3,5,7,9}
print(set1.union(set2))
print(set1 | set2)
print(set1.intersection(set2))
print(set1 & set2)
print(set1.difference(set2))
print(set1 - set2)
print(set1.symmetric_difference(set2))
print(set1 ^ set2)

set3 = {1,3,5}
print(set3.issubset(set1))
print(set1.issuperset(set3))
print(set1 == set2)