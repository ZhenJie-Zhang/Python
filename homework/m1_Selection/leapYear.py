# 4.	選擇性敘述的練習-leapYear
# 輸入一西元年，如2015。判斷此年份是否為閏年。
# 提示：每四年一閏，每百年不閏，每四百年一閏，每四千年不閏。
while True:
    print('******************')
    print('判斷此年份是否為閏年')
    year = input('輸入一西元年(MMMM):')
    year = eval(year)
    test = range(1900, 9800, 100)
    print(test)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 4000 != 0):
        print("{:4d}年為「閏年」，當年有366天".format(year))
    else:
        print("{:4d}年為「平年」，當年有365天".format(year))
