'''
@Date    : 2022-07-10
@Author  : Maksim Soloviov
Practical task 1 for lesson 8
1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках класса
реализовать два метода. Первый, с декоратором @classmethod. Он должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу
полученной структуры на реальных данных.
'''


class Date:
    """Date class"""

    str_date: str
    _date: dict

    def __init__(self, str_date: str) -> None:
        """Date class constructor
        Args:
            str_date (str): Date date in the format 'day-month-year'
        """
        self.str_date = str_date
        self._date = Date.conversion(self.str_date)

    def __str__(self) -> str:
        return '-'.join([
            f"{self._date['day']:02}", f"{self._date['month']:02}",
            f"{self._date['year']}"
        ])

    @classmethod
    def conversion(cls, date: str) -> dict:
        """Преобразование строки в словарь-дату"""
        date_dict = dict(
            zip(["day", "month", "year"], [int(x) for x in date.split("-")]))
        if Date.validate(date_dict):
            return date_dict
        raise ValueError

    @staticmethod
    def validate(date: dict) -> bool:
        """Валидация значений в словаре(дате)"""
        if date["year"] < 0 or date["month"] not in range(1, 13):
            return False
        # check the month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # check the leap year and set 29 in feb
        if (date["year"] % 4 == 0) and ((date["year"] % 100 != 0) or
                                        (date["year"] % 400 == 0)):
            days_in_month[1] = 29
        return date["day"] in range(1, days_in_month[date["month"] - 1] + 1)


def main():
    ''' Main body '''
    try:
        my_date = Date("29-2-1932")
        print(f"{my_date} - correct date")
    except ValueError:
        print("Incorrect date")


if __name__ == '__main__':
    main()
