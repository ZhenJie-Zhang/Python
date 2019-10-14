# 1.	迴圏的練習-expression
# 利用for迴圏計算12-22+32-42+…+492-502的值
total = 0
for i in range(12, 503, 10):
    print('i={:3d}'.format(i), end='\t')
    if i // 10 % 2 == 1:
        total += i
        print('+{:3d}'.format(i), end='\t')
        print('total.now={:5d}'.format(total))
    elif i // 10 % 2 == 0:
        total -= i
        print('-{:3d}'.format(i), end='\t')
        print('total.now={:5d}'.format(total))
print('---------------------------')
print('12-22+32-42+…+492-502的值={}'.format(total))
