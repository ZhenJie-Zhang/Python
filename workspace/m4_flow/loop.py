n = 1
total = 0
while n <= 10:
    total += n
    n += 1
print(total)

total = 0
for n in range(1, 11, 1):
    total += n
print(total)

total = 0
for n in range(1, 101):
    total += n
print(total)

total = 0
for n in range(2, 101, 2):
    total += n
print(total)
total = 0

for n in range(1, 101, 2):
    total += n
print(total)

for i in range(1,10):
    for j in range(1, 10):
        print('{}*{}={}'.format(i,j,i*j),end='\t')
    print()
print('-------------------------------------------------------')

for i in range(1, 10):          # for (i=1; i<10; i++)
    print(i)
print()

for i in range(10, 1, -1):      # for (i=10; i>1; i--)
    print(i)
