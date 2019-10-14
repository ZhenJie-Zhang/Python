def greet(*names):
    print(type(names))
    print(len(names))
    for name in names:
        print('Hello,', name)

greet('Tom', 'Mary', 'Stephen', 'Tina')
greet('Tom', 'Mary', 'Stephen', 'Tina', 'Bob')


def stu(**data):
    print(type(data))
    for key, value in data.items():
        print('{} is {}'.format(key, value))


stu(name='Tom', age=25, mobile='0934111222')
stu(name='Mary', email='mary@gmail.com',age=30,mobile='0939333555')