'''
@Date    : 2022-07-08
@Author  : Maksim Soloviov
Practical task 3 for lesson 7
3. Реализовать программу работы с органическими клетками, состоящими из
ячеек. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству ячеек клетки
(целое число). В классе должны быть реализованы методы перегрузки
арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны
применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток,
соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки
должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
если разность количества ячеек двух клеток больше нуля, иначе выводить
соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки
определяется как произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки
определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий
экземпляр класса и количество ячеек в ряду. Данный метод позволяет
организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где
количество ячеек между \n равно переданному аргументу. Если ячеек на
формирование ряда не хватает, то в последний ряд записываются все
оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в
ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
'''


class Cell():
    """ Клетка """
    size: int

    def __init__(self, size: int) -> None:
        if size > 0:
            self.size = size
        else:
            raise ValueError('Размер клетки должен быть больше 0')

    def __add__(self, other: 'Cell') -> int:
        return Cell(self.size + other.size)

    def __sub__(self, other: 'Cell') -> int:
        result = self.size - other.size
        if result > 0:
            return Cell(result)
        print('Вторая клетка должна быть меньше первой!')
        return None

    def __mul__(self, other: 'Cell') -> int:
        return Cell(self.size * other.size)

    def __truediv__(self, other: 'Cell') -> int:
        return Cell(self.size // other.size)

    def make_order(self, row: int) -> str:
        """ Выстраивание ячеек """
        result = ['*' * row for _ in range(self.size // row)]
        # Избавление от \n в конце. Пока только так придумал
        if self.size % row > 0:
            result.append('*' * (self.size % row))
        return '\n'.join(result)


def main():
    ''' Main body '''
    cell_1 = Cell(10)
    cell_2 = Cell(2)
    print((cell_1 + cell_2).size)
    print((cell_1 - cell_2).size)
    print((cell_1 * cell_2).size)
    print((cell_1 / cell_2).size)
    print(cell_1.make_order(3))


if __name__ == '__main__':
    main()