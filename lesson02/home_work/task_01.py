"""
Author: Maksim Soloviov
Date: 2022-06-16
Python version: 3.10.5

1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно
не запрашивать у пользователя, а указать явно, в программе.
"""

print("Список и типы элементов:")
my_list = [
    None, 1, 2.4, "строка", b"bytes", {1, 2}, [1, 2], (1, 2), {
        "1": 1,
        "2": 2
    }
]

print("Исходный список:\n", my_list)

print("Построчно с типом данных:")
for item in my_list:
    print(item, type(item))