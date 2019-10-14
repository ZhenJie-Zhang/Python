# 6.	選擇性敘述的練習-equation
# 一元二次方程式ax2+bx+c=0。輸入a, b, c三值，並計算方程式的根。
# b^2-4ac > 0，有兩個不相等的實根。
# b^2-4ac = 0，有兩個相等的實根。
# b^2-4ac < 0，則印出”沒有實根”。
import math
import re

while True:
    print('********************************')
    print('一元二次方程式:ax^2+bx+c=0')
    a = input('請輸入a值:')
    b = input('請輸入b值:')
    c = input('請輸入c值:')
    if re.search("^[0-9]*$", a) and re.search("^[0-9]*$", b) and re.search("^[0-9]*$", c):
        a = eval(a)
        b = eval(b)
        c = eval(c)
        print('一元二次方程式:{}*x^2+{:#d}*x+{:#d}=0'.format(a, b, c))

        delta = b ** 2 - 4 * a * c
        print("判別式Δ = {:5.2f} ，".format(delta), end='')
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print('有兩個不相等的實根')
            print('x1 = {:30.28f}'.format(x1))
            print('x2 = {:30.28f}'.format(x2))
        if delta == 0:
            x = -b / (2 * a)
            print('有兩個相等的實根')
            print('x1 = x2 = {:5.2f}'.format(x))
        if delta < 0:
            x1 = complex(-b / (2 * a), +math.sqrt(-delta) / (2 * a))
            x2 = complex(-b / (2 * a), -math.sqrt(-delta) / (2 * a))
            print('沒有實根，但有兩個虛根')
            # print('x1 = {:5.2f}  {:+5.2f}j'.format(x1.real, x1.imag))
            # print('x2 = {:5.2f}  {:+5.2f}j'.format(x2.real, x2.imag))
        continue

    elif a == 'q' or b == 'q' or c == 'q':
        break
    else:
        print('\n輸入錯誤')
        continue
