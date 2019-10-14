# num = int(input('please input a number:'))
# print('{} is {}'.format(num, 'odd' if num % 2 else 'even'))

# try:
#     num = int(input('please input a number:'))
#     print('{} is {}'.format(num, 'odd' if num % 2 else 'even'))
# except ValueError as e:
#     print(e)

try:
    num = int(input('please input a number:'))
    print('{} is {}'.format(num, 'odd' if num % 2 else 'even'))
except ValueError:
    print('請輸入阿拉伯數字')