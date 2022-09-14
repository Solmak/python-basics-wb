"""
Author: Maksim Soloviov
Date: 2022-06-13
Python version: 3.10.5

3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

numstr = input("Введите целое число: ")

print(f'{numstr} + {numstr*2} + {numstr*3} = ', end=' ')
print(f'{int(numstr) + int(numstr*2) + int(numstr*3)}')
