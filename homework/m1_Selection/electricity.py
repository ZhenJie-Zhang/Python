# 3.	選擇性敘述的練習-electricity
# 輸入何種用電和度數，計算出需繳之電費。
# 電力公司使用累計方式來計算電費，分工業用電及家庭用電。
#                    	   家庭用電        工業用電
#    240度(含)以下			0.15元			0.45元
#    240~540(含)度   		0.25元			0.45元
#    540度以上        	    0.45元			0.45元
import re
while True:
    print('********************************')
    print('(1)家庭用電, (2)工業用電 (1 or 2)')
    Type = input('請輸入何種用電:')
    if re.search("[1-2]", Type) and Type.isdigit():
        electricity = input('請輸入用電度數:')
        if re.search("^[0-9]*$", str(electricity)):
            electricity = eval(electricity)
            Type = eval(Type)
            fee = 0
            if Type == 1:
                if electricity <= 240:
                    rate = 0.15
                    fee = rate * electricity
                elif 240 < electricity <= 540:
                    rate = 0.25
                    fee = rate * (electricity - 240) + 0.15 * 240
                elif electricity > 540:
                    rate = 0.45
                    fee = rate * (electricity - 540) + 0.25 * (540 - 240) + 0.15 * 240
            elif Type == 2:
                rate = 0.45
                fee = rate * electricity

            print('電費:{:8.2f}(NTD)'.format(fee))

        elif electricity == 'q':
            break

    elif Type == 'q':
        break

    else:
        print('輸入錯誤')
