print('{0} is {1} years old!'.format('Tom', 30))
print('{1} is {0} years old!'.format(30, 'Tom'))
print('{name} is {age} years old!'.format(name='Tom', age=30))
print('{0} is {age} years old!'.format('Tom', age=30))
print('{} is {} years old!'.format('Tom', 30))

Name = 'Bob'
Age = 15
print('{name} is {age} years old!'.format(name=Name, age=Age))

print('{} {} {}'.format(123, 12345.678, 'Python'))
print('{0} {1} {2}'.format(123, 12345.678, 'Python'))
print('{0} {1:10.2f} {2}'.format(123, 12345.678, 'Python'))
print('{} {:10.2f} {}'.format(123, 12345.678, 'Python'))