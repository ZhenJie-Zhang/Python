import m6_function.mymath
print(dir(m6_function.mymath))
print(m6_function.mymath.mypow(2, 5))
print(m6_function.mymath.myabs(-50))
print(m6_function.mymath.mysum(5, 10))

import m6_function.mymath as math
print(math.mypow(2, 5))
print(math.myabs(-50))
print(math.mysum(5, 10))

from m6_function.mymath import mypow
print(mypow(2, 5))

from m6_function.mymath import mypow as power
print(power(2, 5))