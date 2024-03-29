"""
Author: Maksim Soloviov
Date: 2022-06-16
Python version: 3.10.5

3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето,
осень). Напишите решения через list и dict.
"""

month = 0

while month not in range(1, 13):
    month = input('Введите номер месяца от 1 до 12: ')
    if month.isdigit():
        month = int(month)
        if month not in range(1, 13):
            print('Неверный номер месяца. От 1 до 12, пожалуйста.')
            continue
    else:
        print('Неверный ввод, используйте целые числа')
        month = 0

# Через list
season = [
    'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень',
    'осень', 'осень', 'зима'
]
print(f'{month}-й месяц, это {season[month-1]} (list)')

# Через dict
season = {
    1: 'зима',
    2: 'зима',
    12: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
}
print(f'{month}-й месяц, это {season[month]} (dict)')

# Не придумал как просто, без перебора.
seasons = {
    'зима': (1, 2, 12),
    'весна': (3, 4, 5),
    'лето': (6, 7, 8),
    'осень': (9, 10, 11),
}
for season, months in seasons.items():
    if month in months:
        print(f'{month}-й месяц, это {season} (dict перебор)')
        break
