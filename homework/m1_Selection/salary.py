# 2.	選擇性敘述的練習-salary
# 輸入便利商店工讀生的工作時數，並計算其薪資。
# 60小時以內，時薪120元。
# 61~80小時，以時薪1.25倍計算。
# 81小時以上，以時薪1.5倍計算。
# 說明：薪資以累計方式計算。若工時為90小時，則薪資為60*120 + 20*120*1.25 + 10*120*1.5元。
import re
hr = input('請輸入本月工作時數(hr):')

if re.search("^[0-9]*$", str(hr)):
    hr = eval(hr)
    salary_per_hr = 120
    salary = 0
    if hr >= 0 :
        if hr <= 60:
            salary = hr * salary_per_hr
        elif hr > 60 and hr <= 80:
            salary = (hr - 60) * salary_per_hr * 1.25 + 60 * salary_per_hr
        elif hr > 80:
            salary  =(hr - 80) * salary_per_hr * 1.5 + 20 * salary_per_hr * 1.25 + 60 * salary_per_hr
        print('工作時數:{:8d} (小時)\n本月薪資:{:8,.0f} (NTD$)'.format(hr,salary))
        if hr == 0:
            print('加油好嗎?')
else:
    print('輸入錯誤')