# readline()範例
with open('lang.txt', 'r') as f:
    line = f.readline()
    while line != '':
        print(line, end='')
        line = f.readline()


with open('lang.txt', 'rt') as f:
    line = f.readline()
    while line != '':
        print(repr(line))
        line = f.readline()

print('===========================')
with open('lang.txt', 'rt') as f:
    line = f.readline()
    while line != '':
        print(''.join(repr(line).split('\\n')))
        line = f.readline()

print('===========================')
with open('lang.txt', 'rt') as f:
    line = f.readline()
    while line != '':
        print(repr(line[:-1]))
        line = f.readline()

print('===========================')
with open('lang.txt', 'rt') as f:
    data = f.read()
    print(data, end='')
    print(repr(data))
    print(repr(data[:-1]).strip("'").split('\\n'))
    print(','.join(repr(data[:-1]).split('\\n')))
    print(','.join(repr(data[:-1]).split('\\n')).strip("'"))

print('===========================')
with open('lang.txt', 'rt') as f:
    data = f.read()
    print(data, end='')
    print(repr(data))
    print(repr(data[:-1]).replace('\\n', ','))
    print(repr(data[:-1]).replace('\\n', ',').strip("'"))

print('===========================')
with open('lang.txt') as f:
    print(f.read())
    print(f.read(12))
    print(f.read(10))

print('===========================')
with open('lang.txt') as f:
    print(f.readlines())

print('===========================')
with open('lang.txt') as f:
    print(f.readlines(10))

print('===========================')
with open('lang.txt') as f:
    # print(f.read())
    f.seek(11)
    print(f.read(12))
    print('----')


# with open('test.txt', 'rt', encoding="utf-8") as f:
#     line = f.readline()
#     while line != '':
#         print(repr(line))
#         line = f.readline()
