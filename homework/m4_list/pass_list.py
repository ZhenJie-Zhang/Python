# 2.	函數與串列的練習-pass_list
# a~d各小題皆以一函數來處理：為練習串列的參數傳遞，陣列需定義為main()的區域變數，事先將12個數字置於一3 x 4的二維串列中，列印各函數的結果。
# a.	計算所有數字的平均值
# b.	找出12個數字中最大的值
# c.	找出12個數字中最小的值
# d.	計算每組內4個數字的平均值
import random
import numpy

def avg(num):
    total = 0
    count = 0
    for i in range(len(num)):
        for j in range(len(num[i])):
            total += num[i][j]
            count += 1
    return total/count


def max(num):
    for i in range(len(num)):
        for j in range(len(num[i])):
            if i == 0 and j == 0:
                Max = num[0][0]
            if Max>num[i][j]:
                continue
            if Max<num[i][j]:
                Max = num[i][j]
    return Max


def min(num):
    for i in range(len(num)):
        for j in range(len(num[i])):
            if i == 0 and j == 0:
                Min = num[0][0]
            if Min>num[i][j]:
                Min = num[i][j]
            if Min<num[i][j]:
                continue
    return Min


def avgGroup(num):
    total = 0
    sum = []
    count = 0
    for i in range(len(num)):
        total = 0
        for j in range(len(num[i])):
            if j == 0:
                count = 0
            total += num[i][j]
            count += 1
        sum.append(total/count)
    return sum


def main():
    col = 4
    row = 3
    num = [[random.randint(1, 100) for i in range(col)] for i in range(row)]
    print(num)
    print('平均數:{:4.2f}'.format(avg(num)))
    print('最大值:{:<5d}'.format(max(num)))
    print('最小值:{:<5d}'.format(min(num)))
    print('組平均:{}'.format(avgGroup(num)))

main()