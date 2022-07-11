'''
@Date    : 2022-07-10
@Author  : Maksim Soloviov
Practical task 7 for lesson 8
7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число». Реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта. Для этого создаёте
экземпляры класса (комплексные числа), выполните сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
'''


class Complex():
    """ Комплексные числа"""
    real: float
    imaginary: float

    def __init__(self, real: int | float, imaginary: int | float) -> None:
        self.real = real
        self.imaginary = imaginary

    def __str__(self) -> str:
        """ Строковое представление"""
        return " ".join([
            f"({self.real}", '+' if self.imaginary >= 0 else '-',
            f"{abs(self.imaginary)}i)"
        ])

    def __add__(self, other: 'Complex') -> 'Complex':
        """ Сложение """
        return Complex(self.real + other.real,
                       self.imaginary + other.imaginary)

    def __mul__(self, other: 'Complex') -> 'Complex':
        """ Умножение """
        return Complex(
            (self.real * other.real) - (self.imaginary * other.imaginary),
            (self.real * other.imaginary) + (self.imaginary * other.real))


def main():
    ''' Main body '''
    cmplx1 = Complex(1, -2)
    cmplx2 = Complex(3, 4)
    print(cmplx1, cmplx2)
    print(cmplx1 + cmplx2)
    print(cmplx1 * cmplx2)


if __name__ == '__main__':
    main()
