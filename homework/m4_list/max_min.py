# 1.	一維串列的練習-max_min
# 事先將10個數字置於串列中，分別找出10個數字中最大的值和最小的值。
# (勿使用現成的函數)


import random

num = [random.randint(1, 100) for i in range(10)]
print('隨機10個數字', num)

# Max = 0
# for i in num:
#     if i > Max:
#         Max = i
#     elif i <= Max:
#         continue
# print(Max)
#
# Min = 100
# for i in num:
#     if i > Min:
#         continue
#     elif i <= Min:
#         Min = i
# print(Min)

for i in range(len(num)):
    if i == 0:
        Max = num[0]
    elif Max>num[i]:
        continue
    elif Max<num[i]:
        Max = num[i]
print(Max)

for i in range(len(num)):
    if i == 0:
        Min = num[0]
    elif Min>num[i]:
        Min = num[i]
    elif Min<num[i]:
        continue
print(Min)
