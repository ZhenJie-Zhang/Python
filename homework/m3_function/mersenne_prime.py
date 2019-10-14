# 4.	函數的練習-mersenne_prime
# 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
# 提示：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。
# 說明：當p=3時，2^3-1=7，故7為Mersenne Prime。


def is_prime(num):
    count_factor = 0
    for factor in range(1, int((num ** 0.5) // 1) + 1):
        if num % factor == 0:
            count_factor += 1
    if count_factor == 1:
        return True
    else:
        return False


def is_mersenne_prime(n):
    p = 1
    if is_prime(n):
        while True:
            if 2 ** p - 1 == n:
                p += 1
                return True
            if 2 ** p - 1 > n:
                break
            p += 1
    return False

print(is_mersenne_prime(3))

n = 2
count = 0
while True:
    if is_mersenne_prime(n):
        print(n)
        count += 1
        if count == 5:
            break
    n += 1



# n = 8191
# p = 1
#
# while is_prime(n):
#     if 2 ** p - 1 == n:
#         print(n)
#     if 2 ** p - 1 > n:
#         break
#     p += 1

# n = 2
# p = 1
# count = 0
# while True:
#     if is_prime(n):
#         while True:
#             if 2 ** p - 1 == n:
#                 print(n)
#                 count += 1
#             elif 2 ** p - 1 > n or count == 5:
#                 break
#             p += 1
#     if count == 5:
#         break
#     n += 1
# print()