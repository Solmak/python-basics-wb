'''
@Date    : 2022-06-22
@Author  : Maksim Soloviov

Practical task 7 for lesson 4
7. Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция вызывается следующим образом:
for el in fact(n). Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''


def fact(num: int):
    """Генератор факториалов чисел от 1 до num

    Args:
        num (int): Верхняя граница вычислений

    Yields:
        (generator)): [1!...n!]
    """
    result = 1
    if num <= 0:
        yield result

    for i in range(1, num + 1):
        result *= i
        yield result


def main():
    ''' Main body '''
    num = 7
    print(f'Факториалы чисел от 1 до {num}')
    for i in fact(num):
        print(i)


if __name__ == '__main__':
    main()
