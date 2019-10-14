# 5.	迴圈的練習-prime
# 輸入一正整數，找出所有小於或等於的質數。
import time

t_0 = time.process_time()
num = 10000
print('小於或等於{}的質數: '.format(num), end="")
count_prime = 0
for test in range(1, num + 1):
    # print(test)
    count_factor = 0
    for factor in range(1, test + 1):
        if test % factor == 0:
            count_factor += 1
            # print(factor)
    if count_factor == 2:
        count_prime += 1
        # if count_prime == 1:
        #     print('{:d}'.format(test), end="")
        # elif count_prime != 1:
        #     print(', {:d}'.format(test), end=" ")
print()
print('共有{}個質數'.format(count_prime))
print(time.process_time() - t_0)

t_0 = time.process_time()
print('小於或等於{}的質數: '.format(num), end="")
count_prime = 0
for test in range(2, num + 1):
    # print(test)
    count_factor = 0
    # print(int((test ** 0.5) // 1))
    for factor in range(1, int((test ** 0.5) // 1)+1):
        if test % factor == 0:
            count_factor += 1
    if count_factor == 1:
        count_prime += 1
        # if count_prime == 1:
        #     print('{:d}'.format(test), end="")
        # elif count_prime != 1:
        #     print(', {:d}'.format(test), end=" ")
print()
print('共有{}個質數'.format(count_prime))
print(time.process_time() - t_0)
