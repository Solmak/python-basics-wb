'''
# @Date    : 2022-06-19
# @Author  : Maksim Soloviov
# @Version : 1.0.0

Practical task 4 for lesson 3
4. Программа принимает действительное положительное число x и целое
отрицательное число y. Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y). При решении задания
нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая
использование цикла.
'''


def my_negative_exponentiation(base: float,
                               exponent: int,
                               algorithm: bool = True) -> float:
    """Возведение числа в отрицательную степень

    Args:
        base (float > 0): Основание
        exponent (int < 0): Показатель степени
        algorithm (bool, optional): Выбор алгоритма. True - оператор **,
            False - вычисление в цикле. Defaults to True.
    """

    if algorithm:
        return base**exponent

    result = 1
    for _ in range(abs(exponent)):
        result /= base
    return result


def main():
    ''' Main body '''
    exp_args = [10.6, -3]
    print(exp_args)
    print("С оператором **:   ", my_negative_exponentiation(*exp_args))
    print("Вычисление в цикле:",
          my_negative_exponentiation(*exp_args, algorithm=False))


if __name__ == '__main__':
    main()
