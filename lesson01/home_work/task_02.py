"""
Author: Maksim Soloviov
Date: 2022-06-13
Python version: 3.10.5

2. Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

total_seconds = int(input("Введите время в секундах: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
