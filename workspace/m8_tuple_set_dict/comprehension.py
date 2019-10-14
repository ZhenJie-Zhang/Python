import time

list1 = [i * 3 for i in range(1, 11)]
print(list1)

set1 = {i * 3 for i in range(1, 11)}
print(set1)

dict1 = {i: i*3 for i in range(1, 11)}
print(dict1)

tuple1 = (i * 3 for i in range(1, 11))
for val in tuple1:
    print(val)

list1 = [i for i in range(50) if i % 2 == 0]
print(list1)
list1 = [i for i in range(50) if i % 2 == 1]
print(list1)
list1 = [i for i in range(50) if i % 2]
print(list1)
list1 = [i for i in range(50) if not(i % 2)]
print(list1)


x = (i * i for i in range(10))
print(x)
for y in x:
    print(y)
x = [i * i for i in range(10)]
print(x)
print('*********************************************')
N = 100
# t_0 = time.process_time()
# list1 = [p for p in range(2,N+1) if 0 not in [p%d for d in range(2,p)]]
# print(list1)
# print(time.process_time() - t_0)

t_0 = time.process_time()
list1 = [p for p in range(2,N+1) if 0 not in [p%d for d in range(2,int((p ** 0.5) // 1)+1)]]
print(list1)
print(time.process_time() - t_0)