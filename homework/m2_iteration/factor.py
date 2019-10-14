# 2.	迴圏的練習-factor
# 輸入一正整數，求其所有的因數。
# 說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36。
import random

num = random.randint(1, 100)
print('{:3d}的因數為 '.format(num), end="")
for i in range(1, num+1):
    # print(i)
    if num % i == 0:
        if num != i:
            print(i, end=", ")
        if num == i:
            print(i)

print('{:3d}的因數為 '.format(num), end="")
for i in range(1, int((num ** 0.5) // 1)+1):

    # print(i)
    if num % i == 0:
        factorCouple = int(num / i)
        if num != i:
            if i != factorCouple:
                print(i, factorCouple, end=", ")
            elif i == factorCouple:
                print()


# print('{:3d}的因數為 '.format(num), end="")
# factor = 0
# while True:
#     factor += 1
#     if num % factor == 0:
#         print(factor, end=", ")
#     if num == factor:
#         break
# print()
