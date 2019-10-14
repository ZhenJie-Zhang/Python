# 3.	綜合練習-poker
# 經由亂數發撲克牌(52張)，分為四組列印出來。
import random
from operator import itemgetter

suit = '♣♦♥♠'
face = 'AJQK'
pokerRank = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']


class poker:
    def random(self):
        self.num = []
        while True:
            num = random.randint(0, 51)
            if num not in self.num:
                self.num.append(num)
                if len(self.num) == 52:
                    break
        self.group = []
        for i in range(len(self.num)):
            if i % 13 == 0:
                self.group.append([])
            self.group[i // 13].append(self.num[i])
        return self.group

    def view(self, mode=1):
        self.mode = mode
        p = []
        for i in range(len(self.group)):
            p.append([])
            for j in range(len(self.group[i])):
                if self.mode == 1:
                    p[i].append(suit[self.group[i][j] // 13] + pokerRank[self.group[i][j] % 13])
                elif self.mode == 0:
                    p[i].append(self.group[i][j])
                print(p[i][j], end="\t")
            print()
        print('-------------------------------------------------')
        return p

    def Sort(self):
        code = []
        self.sort = []
        for i in range(len(self.group)):
            code.append([])
            for j in range(len(self.group[i])):
                code[i].append([])
                code[i][j].append(self.group[i][j] // 13)
                code[i][j].append(self.group[i][j] % 13)
            code[i].sort(key=itemgetter(1, 0))
            # self.sort.append([])
            for j in range(len(self.group[i])):
                self.group[i][j] = code[i][j][0] * 13 + code[i][j][1]
        return self.group

    def __str__(self):
        return '{}\n'.format(self.num)


def main():
    card = poker()
    card.random()
    card.view(mode=0)
    card.view()
    card.Sort()
    # card.view(mode=0)
    card.view()


main()
