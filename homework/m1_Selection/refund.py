# 5.	選擇性敘述的練習-refund
# 輸入在某商店購物應付金額與實付金額。
# 實付金額小於應付金額，則印出”金額不足”。
# 實付金額等於應付金額，則印出”不必找錢”。
# 實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
# 假設幣值只有1000, 500, 100元紙鈔和50, 10, 5, 1元硬幣。
# 說明：若買了132元的商品，付1000元，應找回一張500元，三張100元，一個50元硬幣，一個10元硬幣，一個5元硬幣和三個1元硬幣。
import random

while True:
    payable = random.randint(1, 5000)
    paid = random.randint(1, 5000)
    if payable <= paid:
        break
print('應付金額:{:5d}(NTD)'.format(payable))
print('實付金額:{:5d}(NTD)'.format(paid))

if payable > paid:
    print('金額不足')
elif payable == paid:
    print('不必找錢')
elif payable < paid:
    # paid -= payable
    change = paid - payable
    print('應找零錢:{:5d}(NTD)'.format(change))
    print('1000元鈔:{:2d}張'.format(change // 1000), end="\t")
    change %= 1000
    print('未找餘額:{:5d}(NTD)'.format(change))
    print(' 500元鈔:{:2d}張'.format(change // 500), end="\t")
    change %= 500
    print('未找餘額:{:5d}(NTD)'.format(change))
    print(' 100元鈔:{:2d}張'.format(change // 100), end="\t")
    change %= 100
    print('未找餘額:{:5d}(NTD)'.format(change))
    print('  50元幣:{:2d}個'.format(change // 50), end="\t")
    change %= 50
    print('未找餘額:{:5d}(NTD)'.format(change))
    print('  10元幣:{:2d}個'.format(change // 10), end="\t")
    change %= 10
    print('未找餘額:{:5d}(NTD)'.format(change))
    print('   5元幣:{:2d}個'.format(change // 5), end="\t")
    change %= 5
    print('未找餘額:{:5d}(NTD)'.format(change))
    print('   1元幣:{:2d}個'.format(change // 1), end="\t")
    change %= 1
    print('未找餘額:{:5d}(NTD)'.format(change))
else:
    print('輸入錯誤')
