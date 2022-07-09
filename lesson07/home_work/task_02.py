'''
@Date    : 2022-07-08
@Author  : Maksim Soloviov
Practical task 2 for lesson 7
2. Реализовать проект расчёта суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая может
иметь определённое название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для
пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить
работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике
полученные на этом уроке знания: реализовать абстрактные классы для
основных классов проекта, проверить на практике работу декоратора
@property.
'''
from abc import ABC, abstractmethod


class Clothes(ABC):
    """ Абстрактный класс одежды """

    title: str

    @abstractmethod
    def material_count(self):
        """ Подсчет расхода ткани """
        pass


class Coat(Clothes):
    """ Пальто """
    size: int

    def __init__(self, title: str, size: int) -> None:
        super().__init__()
        self.title = title
        self.size = size

    @property
    def material_count(self) -> float:
        return self.size / 6.5 + .5


class Suit(Clothes):
    """ Костюм """
    heigh: float

    def __init__(self, title: str, heigh: float) -> None:
        super().__init__()
        self.title = title
        self.heigh = heigh

    @property
    def material_count(self) -> float:
        return self.heigh * 2 + .3


class Orders(Clothes):
    """ Заказы одежды """

    def __init__(self, orders: list) -> None:
        self.orders = orders

    @property
    def material_count(self):
        return sum(order.material_count for order in self.orders)


def main():
    ''' Main body '''
    order1 = Coat('Летнее пальто', 52)
    order2 = Coat('Осеннее пальто', 44)
    order3 = Suit('Костюм раз', 1.64)
    order4 = Suit('Костюм два', 1.86)
    orders = Orders([order1, order2, order3, order4])

    print(f'{order1.title}: {order1.material_count:.2f}')
    print(f'{order2.title}: {order2.material_count:.2f}')
    print(f'{order3.title}: {order3.material_count:.2f}')
    print(f'{order4.title}: {order4.material_count:.2f}')
    print(f'ИТОГО: {orders.material_count:.2f}')


if __name__ == '__main__':
    main()
