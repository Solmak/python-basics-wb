'''
# @Date    : 2022-06-19
# @Author  : Maksim Soloviov
# @Version : 1.0.0

Practical task 3 for lesson 3
3. Реализовать функцию my_func(), которая принимает три позиционных
аргумента и возвращает сумму наибольших двух аргументов.
'''


def sum_max_two(number1, number2, number3):
    """Вычисление суммы двух наибольших из трех
    Args:
        number1 (int or float): Число 1
        number2 (int or float): Число 2
        number3 (int or float): Число 3
    Returns:
        (int or float): Сумма двух бОльших чисел
    """
    return sum([number1, number2, number3]) - min([number1, number2, number3])


def main():
    ''' Main body '''
    # Опять не беспокоим пользователя, раз не просят
    three = [312, 100, 17]
    print(three)
    print(sum_max_two(*three))


if __name__ == '__main__':
    main()
