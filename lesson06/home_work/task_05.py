'''
@Date    : 2022-07-03
@Author  : Maksim Soloviov
Practical task 5 for lesson 6
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого
класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для
каждого экземпляра.
'''


class Stationery:
    """Канцтовары"""

    title: str

    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        """Отрисовка"""
        return "Запуск отрисовки"


class Pen(Stationery):
    """Ручка"""

    def draw(self) -> None:
        return f"{super().draw()} чернилами"


class Pencil(Stationery):
    """Карандаш"""

    def draw(self) -> None:
        return f"{super().draw()} грифелем"


class Handle(Stationery):
    """Маркер"""

    def draw(self) -> None:
        return f"{super().draw()} толстыми линиями"


def main():
    ''' Main body '''
    stationers = [
        Stationery("Что-то рисующее"),
        Pen("Ручка"),
        Pencil("Карандаш"),
        Handle("Маркер"),
    ]
    for something in stationers:
        print(f'{something.title}: {something.draw()}')


if __name__ == '__main__':
    main()
