# 1.	選擇性敘述的練習-season
# 輸入月份1~12月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。
import re

month = eval(input('請輸入月份(1~12):'))

if re.search("^(0?[1-9]|1[012])$", str(month)):
    print('{}月為'.format(month), end='')
    if month >=1 and month <= 3:
        print('春季')
    if month >=4 and month <= 6:
        print('夏季')
    if month >=7 and month <= 9:
        print('秋季')
    if month >=10 and month <= 12:
        print('冬季')
else:
    print('輸入錯誤')