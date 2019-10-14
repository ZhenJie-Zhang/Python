# 5.	函數的練習-convert
# 輸入一整數，寫兩個函數分別為to_binary(n)和to_hexadecimal(n)用來將n轉換成二進制和十六進制的值。(勿使用任何現成的函數)


def to_binary(n):
    count = 0
    binary = 0
    while True:
        if n > 0:
            n, digit = divmod(n, 2)
            binary += digit * 10 ** count
            count += 1
        if n == 0:
            break
    return binary


def to_hexadecimal(n):
    if n == 0:
        return '0'
    hexa = ''
    while True:
        if n > 0:
            n, digit = divmod(n, 16)
            if digit >= 10:
                if digit == 10:
                    hexa = 'A' + hexa
                elif digit == 11:
                    hexa = 'B' + hexa
                elif digit == 12:
                    hexa = 'C' + hexa
                elif digit == 13:
                    hexa = 'D' + hexa
                elif digit == 14:
                    hexa = 'E' + hexa
                elif digit == 15:
                    hexa = 'F' + hexa
            elif digit < 10:
                hexa = str(digit) + hexa
        if n == 0:
            break
    return hexa


def toBin(dec):
    x = (dec % 2)
    digits = "01"
    rest = dec // 2
    if (rest == 0):
        return digits[x]
    return toBin(rest) + digits[x]


def toHex(dec):
    x = (dec % 16)
    digits = "0123456789ABCDEF"
    rest = dec // 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]

numbers = [0, 11, 16, 32, 33, 41, 45, 678, 574893]
print([to_binary(x) for x in numbers])
print([toBin(x) for x in numbers])
print([bin(x) for x in numbers])
print([to_hexadecimal(x) for x in numbers])
print([toHex(x) for x in numbers])
print([hex(x) for x in numbers])

# num = 10
# binary = 0
# while True:
#     # print(num)
#     num %= 2
#     if num < 2:
#         binary = num * 10
#     if num == 0:
#         binary += num
#         break
# print(binary)

# num = 437
# digit_0 = 0
# count = 0
# binary = 0
# print('{:b}'.format(num))
# while True:
#     if num > 0:
#         num, digit = divmod(num, 2)
#         if digit_0 == 0:
#             binary += (digit_0 + digit * 10 ** count)
#         elif digit_0 == 1:
#             binary += digit * 10 ** count
#         digit_0 = digit
#         count += 1
#     if num == 0:
#         break
# print(binary)

# num = 437
# count = 0
# binary = 0
# print('{:b}'.format(num))
# while True:
#     if num > 0:
#         num, digit = divmod(num, 2)
#         binary += digit * 10 ** count
#         count += 1
#     if num == 0:
#         break
# print(binary)

# num = 456465
# digit_0 = 0
# count = 0
# hexa = ''
# print('{:X}'.format(num))
# while True:
#     if num > 0:
#         num, digit = divmod(num, 16)
#         if digit >= 10:
#             # for i in range(6):
#             #     if digit % 10 == i:
#             #         hexa = str(i) + hexa
#             if digit % 10 == 0:
#                 hexa = 'A' + hexa
#             elif digit % 10 == 1:
#                 hexa = 'B' + hexa
#             elif digit % 10 == 2:
#                 hexa = 'C' + hexa
#             elif digit % 10 == 3:
#                 hexa = 'D' + hexa
#             elif digit % 10 == 4:
#                 hexa = 'E' + hexa
#             elif digit % 10 == 5:
#                 hexa = 'F' + hexa
#         elif digit < 10:
#             hexa = str(digit) + hexa
#     if num == 0:
#         break
# print(hexa)

