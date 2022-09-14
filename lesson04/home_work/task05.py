'''
@Date    : 2022-06-22
@Author  : Maksim Soloviov

Practical task 5 for lesson 4
5. Реализовать формирование списка, используя функцию range() и
возможности генератора. В список должны войти чётные числа от 100 до
1000 (включая границы). Нужно получить результат вычисления произведения
всех элементов списка. Подсказка: использовать функцию reduce().
'''
from functools import reduce


def main():  # sourcery skip: identity-comprehension
    ''' Main body '''
    # Не понимаю зачем тут "генератор, как его называют :)"
    # если можно просто list(range(100, 1001, 2))
    source_list = [i for i in range(100, 1001, 2)]

    list_total = reduce(lambda total, multiplier: total * multiplier,
                        source_list)
    print(f'Произведение всех элементов: {list_total}')

    print('Проверил c 2 до 10, сходится, а то уж очень большое %)')
    source_list = list(range(2, 11, 2))
    print(source_list)
    print(reduce(lambda total, multiplier: total * multiplier, source_list))


if __name__ == '__main__':
    main()
