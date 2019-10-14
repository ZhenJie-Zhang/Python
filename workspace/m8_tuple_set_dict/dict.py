dict1 = {}
dict1 = {'name':'Tom', 'age':24, 'mobile':'0934111222'}
print(dict1['name'])
print(dict1.get('age'))

for key in dict1:
    print('{}: {}'.format(key, dict1[key]))

print(list(dict1.keys()))
print(tuple(dict1.values()))
print(tuple(dict1.items()))

for key, value in dict1.items():
    print('{}: {}'.format(key, value))

print(len(dict1))
print('name' in dict1)
dict2 = {'age':25, 'mobile':'0934111222', 'name':'Tom'}
print(dict2 == dict1)

dict1['email'] = 'tom@gmail.com'
print(dict1)
del dict1['age']
print(dict1)
print(dict1.pop('email'))
print(dict1)
print(dict1.popitem())
print(dict1)
dict1.clear()
print(dict1)

dict1 = dict2.copy()
print(dict1)
dict1['name'] = 'Mary'
dict2['salary'] = 42000
print(dict1)
print(dict2)
dict1.update((dict2))
print(dict1)
print(dict2)
