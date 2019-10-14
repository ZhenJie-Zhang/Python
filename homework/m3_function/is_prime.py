# 2.	函數的練習-is_prime
# 寫一函數is_prime(n)用來判斷n是否為質數。


def is_prime(num):
    count_factor = 0
    for factor in range(1, int((num ** 0.5) // 1) + 1):
        if num % factor == 0:
            count_factor += 1
    if count_factor == 1:
        return True
    else:
        return False


print(is_prime(8))
num = 100
for i in range(1, num + 1):
    if is_prime(i):
        if i == 1:
            print(i, end='')
        if i != 1:
            print(', {}'.format(i), end='')
print()
