try:
    num = int(input('please input a number(0~100):'))
    if 0 <= num <= 100:
        print('score is {}'.format(num))
    else:
        raise ValueError
except ValueError:
    print('please input a integer(0~100):')