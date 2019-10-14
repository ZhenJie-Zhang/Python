# 3.	迴圏的練習-perfect_number
# 一個數字若等於其所有因數的總和，則此數為perfect number。
# 找出100以內所有的完美數。
# 說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。
import time
num = 100
# t_0 = time.process_time()
# for test in range(1, num + 1):
#     factor_sum = 0
#     for factor in range(1, test):  # 不包含自己的因數
#         if test % factor == 0:
#             factor_sum += factor
#             # print(test, factor)
#     if test == factor_sum:
#         print('{:3d} ='.format(test), end="")
#         for factor_print in range(1, test):  # 列出不包含自己的因數
#             if factor_print == 1:
#                 print('{:^3d}'.format(factor_print), end="")
#             elif test % factor_print == 0:
#                 print('+{:^3d}'.format(factor_print), end="")
#         print()
# print(time.process_time() - t_0)

t_0 = time.process_time()
# num = 10000
for test in range(1, num + 1):
    factor_sum = 0
    for factor in range(1, test):
        if test % factor == 0:
            factor_sum += factor
    if test == factor_sum:
        print('{:3d}'.format(test))
print('執行時間:', time.process_time() - t_0)

t_0 = time.process_time()
# num = 10000
for test in range(2, num + 1):
    factor_sum = 0
    for factor in range(1, int((test ** 0.5) // 1)+1):
        if test % factor == 0:
            factorCouple = int(test / factor)
            factor_sum += factor
            if factorCouple != factor and factorCouple != test:
                factor_sum += factorCouple
    if test == factor_sum:
        print('{:3d}'.format(test))
print('執行時間:', time.process_time() - t_0)

# t_0 = time.process_time()
# # num = 10000
# test = 1
# factor = 1
# factor_sum = 0
# while True:
#     if test <= num:
#         if factor < test:
#             if test % factor == 0:
#                 factor_sum += factor
#             factor += 1
#             continue
#         if test == factor_sum:
#             print('{:3d}'.format(test))
#         test += 1
#         factor = 1
#         factor_sum = 0
#     if test > num:
#         break
# print(time.process_time() - t_0)