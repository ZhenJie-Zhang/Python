# 1.	綜合的練習-check_id
# 寫一函數is_id (_id)用來判斷_id是否為正確身份証字號。

def is_id(_id = 'A123456789'):
    if len(_id) == 10 and _id.isalnum() and _id[0].isupper() and _id[0] not in 'LRSY' and _id[1] in ['1', '2']:
        areaCode = dict(A=10, B=11, C=12, D=13, E=14, F=15, G=16, H=17, I=34, J=18, K=19, L=20, M=21,
                        N=22, O=35, P=23, Q=24, R=25, S=26, T=27, U=28, V=29, W=32, X=30, Y=31, Z=33)
        idCode = str(areaCode[_id[0]]) + _id[1:]
        checkCode = '19876543211'
        sum = 0
        for i in range(11):
            sum += int(idCode[i]) * int(checkCode[i])
        if sum % 10 == 0:
            return True
    return False
