# 3.	綜合練習-poker
# 經由亂數發撲克牌(52張)，分為四組列印出來。


import random
suit = '♠♥♣♦'
face = 'AJQK'
x = []
while True:
    num = random.randint(0, 51)
    if num not in x:
        x.append(num)
        if len(x) == 52:
            break

pokerGroup = []
for i in range(len(x)):
    if i % 13 == 0:
        pokerGroup.append([])
    pokerGroup[i//13].append(x[i])
    if i % 13 == 12:
        pokerGroup[i // 13].sort()

# #檢查用
# for i in range(len(pokerGroup)):
#     for j in range(len(pokerGroup[i])):
#         print(pokerGroup[i][j],end="\t")
#     print()

for i in range(len(pokerGroup)):
    for j in range(len(pokerGroup[i])):
        pokerGroup[i][j] = suit[pokerGroup[i][j]//13] + (str(pokerGroup[i][j] % 13 + 1)
                            if pokerGroup[i][j] % 13 < 10 and pokerGroup[i][j] % 13 != 0
                            else face[pokerGroup[i][j] % 13 % 9])
        print(pokerGroup[i][j],end="\t")
    print()
