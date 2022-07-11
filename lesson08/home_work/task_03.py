'''
@Date    : 2022-07-10
@Author  : Maksim Soloviov
Practical task 3 for lesson 8
3. Создайте собственный класс-исключение, который должен проверять
содержимое списка на наличие только чисел. Проверить работу исключения
на реальном примере. Запрашивать у пользователя данные и заполнять
список необходимо только числами. Класс-исключение должен контролировать
типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются
бесконечно, пока пользователь сам не остановит работу скрипта, введя,
например, команду «stop». При этом скрипт завершается, сформированный
список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить
только числа и строки. Во время ввода пользователем очередного элемента
необходимо реализовать проверку типа элемента. Вносить его в список,
только если введено число. Класс-исключение должен не позволить
пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
'''


class NumberValidationError(Exception):
    """ Not valid number exception """
    err_number: str

    def __init__(self, err_number: str) -> None:
        super().__init__(self)
        self.err_number = err_number

    def __str__(self) -> str:
        return f'NumberValidationError: "{self.err_number}" is not valid number.'


def convert_number(number: str) -> float | int:
    """ Конвертирование строки в число"""
    egg_number = number
    if egg_number[0] == '-':
        egg_number = egg_number[1:]
    if egg_number.replace('.', '', 1).isdigit():
        return float(number) if number.count('.') == 1 else int(number)
    else:
        raise NumberValidationError(number)


def main():
    ''' Main body '''
    counter = 1
    numbers = []
    user_input = ''

    print('Для выхода наберите "exit"')
    while user_input != 'exit':

        user_input = input(f'Введите число {counter}: ')
        if user_input.lower() == 'exit':
            continue

        try:
            numbers.append(convert_number(user_input))
        except NumberValidationError as exc:
            print(exc)
        else:
            counter += 1

    print(f"""\nВы закончили ввод.
        Введенный список:
        {numbers}""")


if __name__ == '__main__':
    main()
