# 4.	迴圏的練習-amstrong
# Armstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
# 找出所有的Amstrong數。
# 說明：153=1^3+5^3+3^3，故153為Amstrong數。
num = 999

for test in range(100, num + 1):
    digit100 = test // 100
    digit10 = test % 100 // 10
    digit1 = test % 10
    # print(digit100, digit10, digit1)
    Cube_Sum = digit100 ** 3 + digit10 ** 3 + digit1 ** 3
    # print(Digit_cube_sum)
    if test == Cube_Sum:
        print('{} = {}^3 + {}^3 + {}^3，所以是Armstrong數'.format(Cube_Sum, digit100, digit10, digit1))
