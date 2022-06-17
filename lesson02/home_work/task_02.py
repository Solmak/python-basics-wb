"""
Author: Maksim Soloviov
Date: 2022-06-16
Python version: 3.10.5

2. Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""

my_list = []
user_input = None
el_counter = 0

# Вводим список немного более сложным способом чем input().split()
print("Введите минимум два элемента списка.")
print("Чтобы закончить  ввод просто нажмите Enter.")
while user_input != '':
    user_input = input(f"Введите элемент № {el_counter + 1}: ")
    if user_input == '':
        break
    el_counter += 1
    my_list.append(user_input)

if el_counter < 2:
    print('Вы задали слишком мало элементов списка')
    exit()

print(f"Количество заданных элементов списка: {el_counter}")
print(f"Введенный список: \n{my_list}")

# Начинаем менять местами
i = 0
while i < len(my_list) - 1:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print(f"Модифицированный список: \n{my_list}")
print("\n")
