# 4.	三維串列的練習-rain
# 輸入一字串，字串為”all” 表示計算60個月的總平均降雨量，”year”、”season”和”month”
# 分別表示計算某年、某季或某月的平均降雨量。
# 若為後三者，再輸入一個正整數表示那一年、那一季或那一月。
# 說明：5年12個月的降雨量以三維陣列形式事先給好60個浮點數
# 需做誤錯處理：
# a.	輸入除了”all”、”year”、”season”和”month”以外的字串
# b.	若輸入”year”，而正整數輸入1至5以外的數字
# c.	若輸入”season”，而正整數輸入1至4以外的數字
# d.	若輸入”month”，而正整數輸入1至12以外的數字
import random

def question():
    print('''4.	三維串列的練習-rain
    輸入一字串，字串為”all” 表示計算60個月的總平均降雨量，”year”、”season”和”month”
    分別表示計算某年、某季或某月的平均降雨量。
    若為後三者，再輸入一個正整數表示那一年、那一季或那一月。
    說明：5年12個月的降雨量以三維陣列形式事先給好60個浮點數
    需做誤錯處理：
    a.	輸入除了”all”、”year”、”season”和”month”以外的字串
    b.	若輸入”year”，而正整數輸入1至5以外的數字
    c.	若輸入”season”，而正整數輸入1至4以外的數字
    d.	若輸入”month”，而正整數輸入1至12以外的數
    ------------------------------------------------''')

def month(num):
    total = 0
    count = 0
    for i in range(len(num)):
        for j in range(len(num[i])):
            for k in range(len(num[i][j])):
                total += num[i][j][k]
                count += 1
    return total / count


def season(num):
    total = 0
    sum = []
    count = 0
    for i in range(len(num)):
        total = 0
        for j in range(len(num[i])):
            if j == 0:
                sum.append([])
            for k in range(len(num[i][j])):
                if k == 0:
                    count = 0
                    total = 0
                total += num[i][j][k]
                count += 1
            sum[i].append(total / count)
    return sum

def seasonOnly(num, index):
    total = 0
    count = 0
    for i in range(len(num)):
        for k in range(len(num[i][index])):
            total += num[i][index][k]
            count += 1
    return total / count

def monthOnly(num, index):
    total = 0
    count = 0
    for i in range(len(num)):
        total += num[i][index // 3][index % 3]
        count += 1
    return total / count

def year(num, index):
    total = 0
    sum = []
    count = 0
    for i in range(len(num)):
        for j in range(len(num[i])):
            for k in range(len(num[i][j])):
                total += num[i][j][k]
                count += 1
        sum.append(total / count)
        count = 0
        total = 0
    return sum[index]


def Print3DList(data):
    for i in data:
        for j in i:
            for k in j:
                print(k, end='\t')
        print()


def Print2DList(data):
    for i in data:
        for j in i:
            print('{:.2f}'.format(j), end='\t')
        print()


def Print1DList(data):
    for i in data:
        print('{:.2f}'.format(i), end='\t')
    print()


# months = 12
# years = 5
# # rainData = [[[random.uniform(90, 800) for i in range(months//4)] for j in range(4)] for k in range(years)]
# rainData = [[[random.randint(90, 800) for i in range(months//4)] for j in range(4)] for k in range(years)]
#
# print('降雨量:{}'.format(rainData))
# Print3DList(rainData)
# print('總平均降雨量:{:.2f}'.format(month(rainData)))
# print('季平均:{}'.format(season(rainData)))
# # print('每季平均:')
# Print2DList(season(rainData))
# print('每年平均:')
# Print1DList(year(rainData))

# n = 0
# count = 0
# total = 0
# for i in range(len(season(rainData))):
#     total += season(rainData)[i][n]
#     count += 1
# print(total/count)

def main():
    # question()
    months = 12
    years = 5
    rainData = [[[random.uniform(90, 800) for i in range(months//4)] for j in range(4)] for k in range(years)]
    # rainData = [[[random.randint(90, 800) for i in range(months // 4)] for j in range(4)] for k in range(years)]
    # Print3DList(rainData)
    while True:
        try:
            keyword = input('請輸入查詢關鍵字:')
            # keyword = 'month'
            keywords = ["all", "year", "season", "month"]
            if keyword not in keywords:
                raise ValueError
            elif keyword == "all":
                print('總平均降雨量:{:.2f}'.format(month(rainData)))
            elif keyword == 'year':
                num = eval(input('請輸入查詢年分(1~5):'))
                if 1 <= num <= 5 and str(num).isdigit():
                    print('第{}年的年降雨量:{:.2f}'.format(num, year(rainData, num - 1)))
                else:
                    print('請輸入(1~5)的其中一個整數')
            elif keyword == 'season':
                num = eval(input('請輸入查詢季節(1~4):'))
                if 1 <= num <= 4 and str(num).isdigit():
                    seasonName = '春夏秋冬'
                    print('{}季的季降雨量:{:.2f}'.format(seasonName[num - 1], seasonOnly(rainData, num - 1)))
                else:
                    print('請輸入(1~4)的其中一個整數')
            elif keyword == 'month':
                num = eval(input('請輸入查詢月分(1~12):'))
                if 1 <= num <= 12 and str(num).isdigit():
                    print('{:2d}月的月降雨量:{:.2f}'.format(num, monthOnly(rainData, num - 1)))
                else:
                    print('請輸入(1~12)的其中一個整數')
        except ValueError:
            print('請輸入以下其中一個關鍵字\n"all", "year", "season", "month"')
        except TypeError:
            print('請輸入(1~5)的其中一個整數')
        except NameError:
            print('請輸入數字查詢')
        except SyntaxError:
            print('''1.請不要使用`!@#$%^&*()_+=-{}|"?><[]\'/.,\n2.請不要英文數字混雜輸入''')

main()