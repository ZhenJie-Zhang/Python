print(17/4)
print(17//4)
print(17%4)
print(2**4)

print('Judy' + ' Wang')
# print( 123 + '456')
print( 123 + int('456')) # explict casting
print( str(123) + '456')

print(-17/4)
print(-17//4)
print(-17%4)
print((4*(-17//4)+(-17%4))==-17)

a = 10
b = a
print(id(a), id(b))
print(id(a) == id(b))
print(id(a) is id(b))
print(a is b)

a = 0b0101
b = 0b1100
c = 0b0010
print('  {:04b}\n& {:04b}\n------\n= {:04b}'.format(a, b, a & b))
print('  {:04b}\n| {:04b}\n------\n= {:04b}'.format(a, b, a | b))
print('  {:04b}\n^ {:04b}\n------\n= {:04b}'.format(a, b, a ^ b))
print('~a = {:05b}\n~b = {:05b}\n------'.format(~a, ~b))
print('a << 2 = {:05b}\nb >> 2 = {:05b}\n------'.format(a << 2, b >> 2))
print('(1 << 5) - 1 = {:05b}\n------'.format((1 << 5) - 1 ))
print('a & -a = {:05b}\n------'.format(a & -a))
print('b & -b = {:05b}\n------'.format(b & -b))
print('c & -c = {:05b}\n------'.format(c & -c))
print('a & -a == a => {}\n------'.format((a & -a) == a))
print('b & -b == b => {}\n------'.format((b & -b) == b))
print('c & -c == c => {}\n------'.format((c & -c) == c))
print('  {:05b} \n| {:05b}\n= {:05b}\n------'.format(c, 1 << 2, c | (1 << 2)))
print('  {:05b} \n& {:05b}\n= {:05b}\n------'.format(b, ~(1 << 2), b & ~(1 << 2)))
print('  {:05b} \n  {:05b}\n= {:05b}\n------'.format(b, -(1 << 2), b - (1 << 2)))
print('{:04b}'.format(0b0010))
print('{:04b}'.format(-0b0010))
print('{:04b}'.format(~0b0010))
print('{:04b}'.format(0b0010 & ~0b0010))
print(2 & 13)
print(2 & 29)
print(2 & ~2)