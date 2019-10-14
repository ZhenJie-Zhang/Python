import math


def my_fun(x,n):
    SUM = 0
    for k in range(1, n + 1):
        SUM += x ** k / math.factorial(k)
    return SUM


print(my_fun(12, 4))