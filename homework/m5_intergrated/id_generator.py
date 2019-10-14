# 2.	綜合的練習-id_generator
# 輸入地區和性別，經由亂數產生一個身份証字號。
import random
from m5_intergrated.check_id import is_id

areaNum = dict(A=10, B=11, C=12, D=13, E=14, F=15, G=16, H=17, I=34, J=18, K=19, L=20, M=21,
               N=22, O=35, P=23, Q=24, R=25, S=26, T=27, U=28, V=29, W=32, X=30, Y=31, Z=33)


x = set(chr(i) for i in range(ord('A'), ord('A')+26))
y = {'L', 'R', 'S', 'Y'}
areaCode = list(x.difference(y))
areaCode.sort()

# area = 'A'
# sex = 1
area = areaCode[random.randint(0, len(areaCode) - 1)]
sex = str(random.randint(1, 2))
generateCode = '1987654321'

# idCode = [random.randint(0, 9) for i in range(7)]
# print(idCode)
# print(''.join(str(i) for i in idCode))

idCode = ''.join(str(i) for i in [random.randint(0, 9) for i in range(7)]) #數字0~9，取7碼形成list，再將list相接成string，存入idCode

sum = 0
for i in range(10):
    sum += int((str(areaNum[area]) + sex + idCode)[i]) * int(generateCode[i])
checkCode = str(10 - sum % 10) if sum % 10 != 0 else '0'

_id = area + sex + idCode + checkCode

is_id(_id)