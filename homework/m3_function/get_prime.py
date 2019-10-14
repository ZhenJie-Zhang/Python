# 3.	函數的練習-prime
# 寫一函數get_prime (n)用來找出第n個質數

def is_prime(num):
    count_factor = 0
    for factor in range(1, int((num ** 0.5) // 1) + 1):
        if num % factor == 0:
            count_factor += 1
    if count_factor == 1:
        return True
    else:
        return False


def get_prime(n):
    count_prime = 0
    num = 2
    while True:
        if is_prime(num):
            count_prime += 1
            if count_prime == n:
                break
        num += 1
    return num


print(get_prime(25))
