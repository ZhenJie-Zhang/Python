def greet(*names):
    print(len(names))
    for name in names:
        print('Hello,', name)
greet(*tuple(input('input:').split()))
greet('Tom', 'Mary', 'Stephen', 'Tina')
tuple1 = ('Tom', 'Mary', 'Stephen', 'Tina')
greet(tuple1)
greet(*tuple1)

str1 = "Python"
greet(str1)
greet(*str1)

def stu(**data):
    for key, value in data.items():
        print('{} is {}'.format(key, value))


stu(name='Tom', age=25, mobile='0934111222')
stu(name='Mary', email='mary@gmail.com',age=30,mobile='0939333555')
dict1 = {'name':'Mary', 'email':'mary@gmail.com','age':30,'mobile':'0939333555'}
stu(**dict1)
