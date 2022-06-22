'''
@Date    : 2022-06-22
@Author  : Maksim Soloviov

Practical task 2 for lesson 4
2. Представлен список чисел. Необходимо вывести элементы исходного
списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
from random import randint


def main():
    ''' Main body '''
    # Формирование исходного списка
    source_list = [randint(1, 100) for _ in range(20)]
    print(source_list)

    # Формирование результирующего списка
    result_list = [
        source_list[i] for i in range(1, len(source_list))
        if source_list[i] > source_list[i - 1]
    ]
    print(result_list)

if __name__ == '__main__':
    main()
