def square(x):
    return x * x


def summary(x, y):
    return x + y


def main():
    result = square(3)
    print(result)
    print(square(5))


def factorial(x):
    total = 1
    for num in range(x,0,-1):
        total *= num
    return total


# main()
# a, b = eval(input('input two number to sum up:'))
# print(summary(a, b))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(10))