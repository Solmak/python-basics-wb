'''
@Date    : 2022-07-08
@Author  : Maksim Soloviov
Practical task 1 for lesson 7
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
конструктора класса (метод __init__()), который должен принимать данные
(список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода
матрицы в привычном виде. Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д.
'''


class Matrix():
    """ Матрица """
    values: list
    _row: int
    _col: int

    def __init__(self, val: list) -> None:
        self.values = val
        # Дополняем 0 до максимума длины строк
        self._row = len(self.values)
        self._col = max(len(row) for row in self.values)
        for row in self.values:
            while len(row) < self._col:
                row.append(0)

    def __str__(self) -> str:
        # TODO генератор?
        # result = ''
        # for i in self.values:
        #     for j in i:
        #         result += f'{j} ' # TODO форматирование в f-строке
        #     result += '\n'
        return '\n'.join([
            ' '.join(list(map(lambda el: f'{el:>5}', row)))
            for row in self.values
        ])

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self._row == other._row and self._col == other._col:
            return Matrix([[
                self.values[row][col] + other.values[row][col]
                for col in range(self._col)
            ] for row in range(self._row)])
        else:
            # Можно сделать дополнение 0 до недостающего
            raise ValueError('Матрицы должны быть одного размера!')


def main():
    ''' Main body '''
    mtx1 = Matrix([[23, 56, 33], [1, 12, 4], [100, 1, 12]])
    print(f'Матрица 1:\n{mtx1}')
    mtx2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    print(f'Матрица 2:\n{mtx2}')
    mtx_s = mtx1 + mtx2
    print(f'Сумма матриц:\n{mtx_s}')


if __name__ == '__main__':
    main()
