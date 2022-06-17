"""
Author: Maksim Soloviov
Date: 2022-06-16
Python version: 3.10.5

5. Реализовать структуру «Рейтинг», представляющую собой набор
натуральных чисел, который не возрастает. У пользователя нужно
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен
разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например,
my_list = [7, 5, 3, 3, 2].
"""


def list_sort(user_list: list, user_number: int) -> None:
    """ Формирование рейтинга самым простым способом

    Args:
        user_list (list): Список с рейтингом
        user_number (int): Новый элемент
    """
    user_list.append(user_number)
    user_list.sort(reverse=True)


def list_insert(user_list: list, user_number: int) -> None:
    """ Формирование извращенным способом
    На случай, если смысл задания потренироваться в работе со списками и
    их индексами

    Args:
        user_list (list): Список с рейтингом
        user_number (int): Новый элемент
    """
    # Стараемся минимизировать перебор
    if user_number > user_list[0]:
        user_list.insert(0, user_number)
    elif user_number < user_list[-1]:
        user_list.append(user_number)
    elif user_list.count(user_number):
        user_list.insert(user_list.index(user_number), user_number)
    else:  # делать нечего, начинаем перебор
        for index, el in enumerate(user_list):
            if user_number > el:
                user_list.insert(index, user_number)
                break


user_list = [12, 9, 7, 6, 2]
print("Чтобы закончить ввод новых элементов, просто нажмите Enter.")
print(f"Исходный рейтинг: {user_list}")

user_number = None
while user_number != '':
    user_number = input("Введите новый элемент рейтинга: ")
    if user_number.isdigit() and int(user_number) > 0:
        list_insert(user_list, int(user_number))
        print(f"Новый рейтинг: {user_list}")
