"""
Author: Maksim Soloviov
Date: 2022-06-13
Python version: 3.10.5

4. Пользователь вводит целое положительное число. Найдите самую большую
цифру в числе. Для решения используйте цикл while и арифметические
операции.
"""


num = int(input("Введите целое число: "))
num_original = num  # для красивого вывода результата

max_digit = 0
while num and max_digit != 9:
    if num % 10 > max_digit:
        max_digit = num % 10
    num //= 10

print(f"Максимальная цифра в числе {num_original}, это {max_digit}")
