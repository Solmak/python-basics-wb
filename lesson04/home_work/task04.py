'''
@Date    : 2022-06-22
@Author  : Maksim Soloviov

Practical task 4 for lesson 4
4. Представлен список чисел. Определите элементы списка, не имеющие
повторений. Сформируйте итоговый массив чисел, соответствующих
требованию. Элементы выведите в порядке их следования в исходном списке.
Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
Результат: [23, 1, 3, 10, 4, 11]
'''
from random import randint


def main():
    ''' Main body '''
    source_list = [randint(1, 30) for _ in range(20)]
    print(f'Исходный: {source_list}')
    result_list = [egg for egg in source_list if source_list.count(egg) == 1]
    print(f'Результат: {result_list}')


if __name__ == '__main__':
    main()
