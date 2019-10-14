a = 123
b = 12345.678
c = 'Python'

print('%d' % a)
print('%5d' % a)
print('%05d' % a)
print('%2d/' % a)
print('%-5d/' % a)
print('%+5d/' % a)
print('%+5d/' % -a)

print('%x' % a)
print('%X' % a)
print('%#x' % a)
print('%#X' % a)
print('%o' % a)
print('%#o' % a)

a = 12345.678
print('%f' % a)
print('%.2f' % a)
print('%10.2f/' % a)
print('%010.2f/' % a)
print('%-10.2f/' % a)

print('%e' % a)
print('%E' % a)
print('%.2e/' % a)
print('%10.2e/' % a)
print('%-10.2e/' % a)

a = 123
print('%c' % a)
print('%s' % a)

a = 'Python'
print('%s/' % a)
print('%10s/' % a)
print('%-10s/' % a)
print('%10r/' % a)
print('%r/' % a)
print(repr(a))
print(a)

print('%10s %10s %10s' % (a, a, a))
print('%10s %10s %10s' % ('Java', 'Java', 'Java'))
print('%10s %10s %10s' % ('C++', 'Java', 'Java'))
print('%-10s %-10s %-10s' % ('C++', 'Java', 'Java'))