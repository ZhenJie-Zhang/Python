# 8.	迴圏的練習-password
# 出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
# 若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
# 若輸入不正確，再次出現”請輸入密碼”的提示。
# 若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。
password = 123
count = 1
while True:
    password_input = input('請輸入密碼，只有三次輸入錯誤的機會:')
    password_input = eval(password_input)
    if password == password_input:
        print('密碼輸入正確，歡迎使用本系統')
        break
    elif password != password_input and count < 3:
        print('密碼輸入不正確，請確認後，再次輸入密碼')
    if count == 3:
        print('密碼輸入超過三次錯誤!，帳號將鎖定，如需解鎖，請電話連絡客服，謝謝')
        break
    count += 1
