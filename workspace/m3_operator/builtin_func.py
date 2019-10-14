print(abs(-5))
print(max(213,13,34,25,4,45,634,-34))
print(min(213,13,34,25,4,45,634,-34))
print(pow(3,4))
print(round(12345.678,0))
print(round(12345.678))
print(round(12345.5,0))
print(round(12346.5))
print('')
print(round(12345.45))
print(round(12346.45,0))
print('')
print(round(12346.465,2))
print(round(12346.475,2))
print(round(12346.485,2))
print('')
print(round(12346.565,2))
print(round(12346.575,2))
print(round(12346.585,2))
print(-1.225*100)
print(round(4.5))
print(round(3.5))
print(round(1.75,1))
print(round(1.65,1))

# https://realpython.com/python-rounding/
# https://docs.python.org/3/library/decimal.html
# https://en.wikipedia.org/wiki/Rounding
# 對稱型四捨五入  flag: ROUND_HALF_UP ; 	Rounding Strategy:Rounding half away from zero
from decimal import *
getcontext()
print(Decimal(0.1))
print(Decimal('0.1'))
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1'))
print(Decimal("1.75").quantize(Decimal("0.0")))
print(Decimal("1.45").quantize(Decimal("0.0")))
print(getcontext().rounding)
getcontext().prec = 2
getcontext().rounding = ROUND_UP
print(getcontext())
getcontext().prec = 28
print(getcontext().rounding)
print(Decimal("1.45").quantize(Decimal("0.0")))
print(Decimal('12346.585').quantize(Decimal('.00'), rounding=ROUND_DOWN))
print(Decimal('12346.585').quantize(Decimal('.00'), rounding=ROUND_UP))
print('')
print(Decimal('12346.575').quantize(Decimal('.00'), rounding=ROUND_HALF_EVEN))
print(Decimal('12346.575').quantize(Decimal('.00'), rounding=ROUND_HALF_UP))
print('')
print(Decimal('12346.585').quantize(Decimal('.00'), rounding=ROUND_HALF_EVEN))
print(Decimal('12346.585').quantize(Decimal('.00'), rounding=ROUND_HALF_UP))
print('')
print(Decimal('12346.595').quantize(Decimal('.00'), rounding=ROUND_HALF_EVEN))
print(Decimal('12346.595').quantize(Decimal('.00'), rounding=ROUND_HALF_UP))