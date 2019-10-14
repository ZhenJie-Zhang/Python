def factorial(num):
    result = 1
    for i in range(num, 0, -1):
        result *= i
    return result


def fac(num):
    if num == 0:
        return 1
    return fac(num-1) * num


def main():
    num = eval(input('input a number:'))
    print('{:2d}! = {:,d}'.format(num, factorial(num)))
    print('{:2d}! = {:,d}'.format(num, fac(num)))

while True:
    main()
