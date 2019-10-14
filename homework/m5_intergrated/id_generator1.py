# 2.	綜合的練習-id_generator
# 輸入地區和性別，經由亂數產生一個身份証字號。
import random
from m5_intergrated.check_id import is_id

sextype = dict(男=1, 女=2)
areaNum = dict(A=10, B=11, C=12, D=13, E=14, F=15, G=16, H=17, I=34, J=18, K=19, L=20, M=21,
               N=22, O=35, P=23, Q=24, R=25, S=26, T=27, U=28, V=29, W=32, X=30, Y=31, Z=33)
colName = ['code', 'value', 'city']
areaTable = [['A', 10, '臺北市'], ['B', 11, '臺中市'], ['C', 12, '基隆市'], ['D', 13, '臺南市'],
             ['E', 14, '高雄市'], ['F', 15, '新北市'], ['G', 16, '宜蘭縣'], ['H', 17, '桃園市'],
             ['I', 34, '嘉義市'], ['J', 18, '新竹縣'], ['K', 19, '苗栗縣'], ['M', 21, '南投縣'],
             ['N', 22, '彰化縣'], ['O', 35, '新竹市'], ['P', 23, '雲林縣'], ['Q', 24, '嘉義縣'],
             ['T', 27, '屏東縣'], ['U', 28, '花蓮縣'], ['V', 29, '臺東縣'], ['W', 32, '金門縣'],
             ['X', 30, '澎湖縣'], ['Z', 33, '連江縣'], ['L', 20, '臺中縣'], ['R', 25, '臺南縣'],
             ['S', 26, '高雄縣'], ['Y', 31, '陽明山管理局']]


def codeToCity(area):
    for i in range(len(areaTable)):
        if areaTable[i][colName.index('code')] == area:
            return areaTable[i][colName.index('city')]


def id_generator(city="", sex=""):
    def cityToCode(city):
        for i in range(len(areaTable)):
            if areaTable[i][colName.index('city')] == city:
                return areaTable[i][colName.index('code')]
    x = set(chr(i) for i in range(ord('A'), ord('A')+26))
    y = {'L', 'R', 'S', 'Y'}
    areaCode = list(x.difference(y))
    areaCode.sort()
    area = areaCode[random.randint(0, len(areaCode) - 1)] if city == "" else cityToCode(city)
    sex = str(random.randint(1, 2)) if sex == "" else str(sextype[sex])
    generateCode = '1987654321'
    idCode = ''.join(str(i) for i in [random.randint(0, 9) for i in range(7)])
    sum = 0
    for i in range(10):
        sum += int((str(areaNum[area]) + sex + idCode)[i]) * int(generateCode[i])
    # checkCode = str(10 - sum % 10) if sum % 10 != 0 else '0'
    checkCode = str(-sum % 10)
    _id = area + sex + idCode + checkCode
    return _id


# print(-121 % 10)
city = '宜蘭縣'
sex = '女'
_id = id_generator(city, sex)
if is_id(_id):
    print('居住地:{}\n性別　:{}性\n依據以上資料產生\n有效身分證字號:{}'.format(city, sex, _id))
_id2 = id_generator()
print('---------------------------------------')
if is_id(_id2):
    print('隨機產生\n有效身分證字號:{}'.format(_id2))
    print('此人出身戶籍地為:{}\n性別　:{}性'.format(codeToCity(_id2[0]), tuple(sextype.items())[int(_id2[1])-1][0]))