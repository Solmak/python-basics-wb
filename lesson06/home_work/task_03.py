'''
@Date    : 2022-07-03
@Author  : Maksim Soloviov
Practical task 3 for lesson 6
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname,position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров.
'''


class Worker:
    """ Работник """
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: float,
                 bonus: float) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """ Должность """

    def get_full_name(self) -> str:
        """ Полное имя """
        return f"{self.name} {self.surname}"

    def get_total_income(self) -> float:
        """ Доход """
        return self._income["wage"] + self._income["bonus"]


def main():
    ''' Main body '''
positions = [
    Position('Kate', 'Brown', 'Cleaner', 300, 50),
    Position('Peter', 'Smith', 'Janitor', 350, 60),
    Position('Leonard', 'Doe', 'Engineer', 785, 250)
]
for person in positions:
    print(f'{person.get_full_name()}, Position: {person.position},',
          f'Income: {person.get_total_income()}')

if __name__ == '__main__':
    main()
