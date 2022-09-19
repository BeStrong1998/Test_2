"""
Домашнее задание №2
Дата и время
1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime
"""

from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, 'russian')


def print_days():
    date_now = datetime.now()

    delta = timedelta(days=30)
    delta_1 = timedelta(days=1)

    print('Вчерашнея дата:', date_now - delta_1)
    print('Сегоднешняя дата:', date_now)
    print('Дата 30 дней назад:', date_now - delta)

def str_2_datetime(date_string):
    res = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print(res)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))





