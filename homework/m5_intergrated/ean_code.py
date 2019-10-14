import random

country_code = ''.join(str(i) for i in [random.randint(0, 9) for i in range(3)])
print(country_code)

issn = ''.join(str(i) for i in [random.randint(0, 9) for i in range(7)])
issn_checkcode = '8765432'
check_digit = -sum([(int(issn[i]) * int(issn_checkcode[i])) for i in range(len(issn_checkcode))]) % 11
check_digit = str(check_digit) if check_digit != 10 else 'X'
issn += check_digit
print('ISSN {}-{}'.format(issn[:4], issn[4:]))


ean = '977' + issn[:7] + '00'
ean_checkcode = '131313131313'
check_digit = -sum([(int(ean[i]) * int(ean_checkcode[i])) for i in range(len(ean_checkcode))]) % 10
ean += str(check_digit)
print('EAN  {}-{}-{}-{}-{}'.format(ean[:3], ean[3:6], ean[6:10], ean[10:12], ean[12]))


isbn = ''.join(str(i) for i in [random.randint(0, 9) for i in range(9)])
isbn_checkcode = '987654321'
check_digit = -sum([(int(isbn[i]) * (int(isbn_checkcode[i]) + 1)) for i in range(len(isbn_checkcode))]) % 11
check_digit = str(check_digit) if check_digit != 10 else 'X'
isbn += check_digit
print('ISBN {}-{}-{}-{}'.format(isbn[:3], isbn[3:7], isbn[7:9], isbn[9]))


ean = '978' + isbn[:9]
ean_checkcode = '131313131313'
check_digit = -sum([(int(ean[i]) * int(ean_checkcode[i])) for i in range(len(ean_checkcode))]) % 10
ean += str(check_digit)
print('EAN  {}-{}-{}-{}-{}'.format(ean[:3], ean[3:6], ean[6:10], ean[10:12], ean[12]))
