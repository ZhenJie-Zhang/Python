# 9.	迴圈敘述的練習-stars
#    畫出下列三種排列的星星圖形
# 1)	*         (2)   * * * * *    (3)  	*
#       * *              * * * *           *  *
#       * * *              * * *          *  *  *
#       * * * *              * *         *  *  *  *
#       * * * * *              *        *  *  *  *  *
print('1)------------------------')
num = 5
for i in range(num):
    for j in range(i+1):
        print('*', end='')
        # print(i, j)
    print()

for i in range(6):
    print('*' * i)
print('2)------------------------')
num = 5
for i in range(num):
    for j in range(1,i+1):
        print(' ', end="")
    for j in range(num,i,-1):
        print('*', end="")
    print()

for i in range(5, 0, -1):
    print(' ' * (5-i) + '*'*i)
for i in range(5):
    print(' ' * i + '*'*(5-i))

print('3)------------------------')
num = 5
for i in range(1, num+1):
    for j in range(num, i, -1):
        print(' ', end="")
    for j in range(0,i):
        print('*', end="")
        print(' ', end="")
    print()
num = 5
for i in range(1, num+1):
    for j in range(num-1, i, -1):
        print(' ', end="")
    for j in range(0, i):
        if i == num and j == 0:
            print('*', end="")
        else:
            print(' ', end="")
            print('*', end="")
    print()
for i in range(1, 6):
    print(' ' * (5-i) + '* ' * i)
for i in range(5):
    print(' ' * (4-i) + '* ' * (i+1))
for i in range(3, -2, -1):
    print(' ' * (i+1) + '* ' * (4-i))
for i in range(4, -1, -1):
    print(' ' * i + '* ' * (5-i))
for i in range(5, 0, -1):
    print(' ' * (i-1) + '* ' * (6-i))
print('------------------------')
