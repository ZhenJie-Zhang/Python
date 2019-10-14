# 4.	日期的練習-my_calendar
# 輸入一個正整數，列印出那一年的年曆。
# 輸入兩個整數，第一個數字代表那一年，第二個數字代表那一月，列印出那一年那一月的月曆。
import datetime
import calendar

# Constants for months referenced later
January = 1
February = 2

# Number of days per month (except for February in leap years)
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isleap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def monthlen(year, month):
    return mdays[month] + (month == February and isleap(year))


def Month(year, month):
    title = datetime.datetime(year, month, 1).strftime("%B") + ' ' + str(year)
    weekname = 'Mo Tu We Th Fr Sa Su'
    print('{:^20s}'.format(title))
    print('{:^20s}'.format(weekname))
    space = datetime.date(year, month, 1).weekday()
    for i in range(monthlen(year, month)):
        if space == 0:
            print('', end='')
        elif i == 0:
            print('  ' * space, ' ' * (space - 1), end='')
        print('{:>2d}'.format(i + 1), end='')
        if (i + space) % 7 < 6:
            print(' ', end='')
        elif (i + space) % 7 == 6:
            print()
    print('\n')


def Year(year):
    for i in range(1, 13):
        Month(year, i)


def my_calendar(*args):
    if len(args) == 1:
        Year(int(args[0]))
    elif len(args) == 2:
        Month(int(args[0]), int(args[1]))
    pass



def main():
    year = 2020
    month = 2
    year1 = 2040

    my_calendar(*tuple(input('input:').split()))
    # Month(year, month)
    # Year(year1)

    # print(calendar.monthrange(year, month))
    # print(calendar.month(year, month))
    # print(calendar.month_name[month])
    # print(calendar.calendar(year))


main()
