'''
@Date    : 2022-07-10
@Author  : Maksim Soloviov
Practical task 2 for lesson 8
2. Создайте собственный класс-исключение, обрабатывающий ситуацию
деления на ноль. Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
'''
class MyZeroDivisionError(Exception):
    """Обработка деления на 0 """

    def __str__(self) -> str:
        return 'MyZeroDivisionError: The divisor cannot be equal to 0'


def main():
    ''' Main body '''
    num1 = input('Введите первое число: ')
    num2 = input('Введите второе число: ')

    try:
        num1 = int(num1)
        if num2 != '0':
            num2 = int(num2)
        else:
            raise MyZeroDivisionError
        print(num1 / num2)
    except MyZeroDivisionError as exc:
        print(exc)
    except ValueError as exc:
        print(exc)

if __name__ == '__main__':
    main()
