a = 123
b = 12345.678
c = 'Python'

print(format(a, 'd'))
print(format(a, '5d'))
print(format(a, '05d'))
print(format(a, '2d'))
print(format(a, '-5d'))
print(format(a, '+5d'))
print(format(a, '+5d'))

print(format(a, 'x'))
print(format(a, 'X'))
print(format(a, '#x'))
print(format(a, '#X'))
print(format(a, 'o'))
print(format(a, '#o'))
print(format(a, 'b'))
print(format(a, '#b'))

a = 12345.678
print(format(a, 'f'))
print(format(a, '.2f'))
print(format(a, '10.2f'))
print(format(a, '10,.2f'))
print(format(a, '010.2f'))
print(format(a, '-10.2f'))

print(format(a, 'e'))
print(format(a, 'E'))
print(format(a, '.2e'))
print(format(a, '10.2e'))
print(format(a, '10.2e'))
print(format(a, '-10.2e'))

a = 123
# print(format(a, 'c'))
# print(format(a, 's'))

a = 'Python'
print(format(a, 's'))
print(format(a, '<10s'))
print(format(a, '*<10s'))
print(format(a, '#<10s'))
print(format(a, '/>10s'))
print(format(a, '\^10s'))
# print(format(a, '10r'))
# print(format(a, 'r/'))
print(repr(a))
print(a)

Name = 'Tina'
Age = 18
print('{name} is {age} years old!'.format(name=Name, age=Age))

print('%10s %10s %10s' % (a, a, a))
print('%10s %10s %10s' % ('Java', 'Java', 'Java'))
print('%10s %10s %10s' % ('C++', 'Java', 'Java'))
print('%-10s %-10s %-10s' % ('C++', 'Java', 'Java'))