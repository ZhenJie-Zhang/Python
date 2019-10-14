# 3.	二維串列的練習-sales
# 某一公司有五種產品A、B、C、D與E，其單價分別為12、16、10、14與15元；而該公司共有三位銷售員，他們在某月份的銷售數量如下所示
# 試計算：
# a.	每一個銷售員的銷售總金額
# b.	有最好業績（銷售總金額最多者）的銷售員
# c.	每一項產品的銷售總金額
# d.	銷售總金額最多的產品


def question(productNo, product, sales):
    print('試計算：')
    for i in range(len(productNo)):
        if i == 0:
            print('銷售員\t|', end='')
        print('商品{}\t|'.format(productNo[i]), end='')
    print()
    print('----------' * len(productNo))
    for i in sales:
        for j in i:
            print('{:^5}\t|'.format(j), end='')
        print()
    print('----------' * len(productNo))
    for i in range(len(productNo)):
        if i == 0:
            print('{:^5}\t|'.format('單價'), end='')
        print('{:^5}\t|'.format(product[i]), end='')
    print()
    print('----------' * len(productNo))

def SalesAmount(product, sales):
    total = 0
    sales_amount = []
    for i in range(len(sales)):
        total = 0
        for j in range(len(product)):
            total += sales[i][j + 1] * product[j]
        sales_amount.append(total)
    print('a.----------------------------------------------')
    print('每一個銷售員的銷售總金額')
    for i in range(len(sales_amount)):
        print('{:>5s}:{:6d}'.format(sales[i][0], sales_amount[i]))

def SalesBest(product, sales):
    total = 0
    sales_amount = []
    for i in range(len(sales)):
        total = 0
        for j in range(len(product)):
            total += sales[i][j + 1] * product[j]
        sales_amount.append(total)
    print('b.----------------------------------------------')
    print('有最好業績的銷售員:{}\n銷售總金額:{}'.format(sales[sales_amount.index(max(sales_amount))][0], max(sales_amount)))

def ProductAmount(productNo, product, sales):
    total = 0
    product_amount = []
    for j in range(len(product)):
        total = 0
        for i in range(len(sales)):
            total += sales[i][j + 1] * product[j]
        product_amount.append(total)
    print('c.----------------------------------------------')
    print('每一項產品的銷售總金額')
    for i in range(len(product_amount)):
        print('商品{:s}:{:6d}'.format(productNo[i], product_amount[i]))

def ProductBest(productNo, product, sales):
    total = 0
    product_amount = []
    for j in range(len(product)):
        total = 0
        for i in range(len(sales)):
            total += sales[i][j + 1] * product[j]
        product_amount.append(total)
    print('d.----------------------------------------------')
    print('銷售總金額最多的產品:商品{:s}\n銷售總金額:{}'.format(productNo[product_amount.index(max(product_amount))], max(product_amount)))

def main():
    productNo = 'ABCDE'
    product = [12, 16, 10, 14, 15]
    sales = [['Jean',33,32,56,45,33], ['Tom',77,33,68,45,23], ['Tina',43,55,43,67,65]]

    question(productNo, product, sales)
    SalesAmount(product, sales)
    SalesBest(product, sales)
    ProductAmount(productNo, product, sales)
    ProductBest(productNo, product, sales)

main()

# print('試計算：')
# for i in range(len(productNo)):
#     if i == 0:
#         print('銷售員\t|', end='')
#     print('商品{}\t|'.format(productNo[i]), end='')
# print()
# print('----------'*len(productNo))
# for i in sales:
#     for j in i:
#         print('{:^5}\t|'.format(j),end='')
#     print()
# print('----------'*len(productNo))
# for i in range(len(productNo)):
#     if i == 0:
#         print('{:^5}\t|'.format('單價'), end='')
#     print('{:^5}\t|'.format(product[i]), end='')
# print()
# print('----------'*len(productNo))


# print('a.----------------------------------------------')
# total = 0
# sales_amount =[]
# for i in range(len(sales)):
#     total = 0
#     for j in range(len(product)):
#         total += sales[i][j+1] * product[j]
#     sales_amount.append(total)
#
# print('每一個銷售員的銷售總金額')
# for i in range(len(sales_amount)):
#     print('{:>5s}:{:6d}'.format(sales[i][0], sales_amount[i]))
# print('b.----------------------------------------------')
# print('有最好業績的銷售員:{}\n銷售總金額:{}'.format(sales[sales_amount.index(max(sales_amount))][0], max(sales_amount)))

# print('c.----------------------------------------------')
# total = 0
# product_amount =[]
# for j in range(len(product)):
#     total = 0
#     for i in range(len(sales)):
#         total += sales[i][j+1] * product[j]
#     product_amount.append(total)
# print('每一項產品的銷售總金額')
# for i in range(len(product_amount)):
#     print('商品{:s}:{:6d}'.format(productNo[i], product_amount[i]))
# print('d.----------------------------------------------')
# print('銷售總金額最多的產品:商品{:s}\n銷售總金額:{}'.format(productNo[product_amount.index(max(product_amount))], max(product_amount)))