'''
# @Date    : 2022-06-19
# @Author  : Maksim Soloviov
# @Version : 1.0.0

Practical task 1 for lesson 3
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''


def my_division(divisible, divisor):
    """Функция деления двух чисел
    Args:
        divisible (int or float): Делимое
        divisor (int or float): Делитель
    Returns:
        float: Частное
    """
    return divisible / divisor


def main():
    ''' Main body '''
    while True:
        try:
            num1 = float(input("Введите Число 1: "))
            num2 = float(input("Введите Число 2: "))
            result = my_division(num1, num2)
        except ZeroDivisionError:
            print("Деление на 0 недопустимо!")
        except ValueError:
            print("Допустимы только числовые аргументы!")
        else:
            print(f"Результат деления {num1} на {num2} равен {result}")
            break


if __name__ == '__main__':
    main()
