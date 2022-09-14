'''
@Date    : 2022-06-22
@Author  : Maksim Soloviov

Practical task 1 for lesson 4
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчёта заработной платы сотрудника. Используйте в нём формулу:
(выработка в часах*ставка в час) + премия. Во время выполнения расчёта
для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv


def payment_calc(working_hours: float,
                 hour_payment: float,
                 bonus: float,
                 for_print: bool = False) -> float:
    """Функция расчета заработной платы сотрудника

    Использует формулу: (выработка в часах*ставка в час) + премия.

    Args:
        working_hours (float): Отработано часов
        hour_payment (float): Ставка за час
        bonus (float): Премия
        for_print (bool, optional): Вывод результатов на экран.
            Defaults to False.

    Returns:
        (float): Сумму к выплате
    """
    result = working_hours * hour_payment + bonus
    if for_print:
        print(f'Отработано часов: {working_hours}',
              f'Почасовая ставка: {hour_payment}',
              f'Премия: {bonus}',
              f'ИТОГО к выплате: {result}',
              sep='\n')
    return result


def main():
    ''' Main body '''
    match len(argv):
        case 1:
            print('Параметры не заданы. Задание № 1 игнорируется.')
        case 4:
            try:    # Не стал в одну строку для читаемости
                working_hours = float(argv[1])
                hour_payment = float(argv[2])
                bonus = float(argv[3])
                payment_calc(working_hours, hour_payment, bonus, for_print=True)
            except ValueError:
                print('Используйте только числа!')
        case _:
            print('Неверное количество параметров')
            print('Параметры: <отработано_часов> <ставка_в_час> <премия>')


if __name__ == '__main__':
    main()
