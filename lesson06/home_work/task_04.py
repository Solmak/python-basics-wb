'''
@Date    : 2022-07-03
@Author  : Maksim Soloviov
Practical task 4 for lesson 6
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните
доступ к атрибутам, выведите результат. Вызовите методы и покажите
результат.
'''
class Car:
    """Базовый класс автомобиля
    """
    name: str
    color: str
    speed: int
    is_police: bool

    def __init__(self, name: str, color: str, speed: int = 0,
                 is_police: bool = False) -> None:
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def info(self) -> str:
        """ Информация об автомобиле """
        police = ' полиции' if self.is_police else ''
        return f'{self.color} {self.name}{police}'

    def show_speed(self) -> None:
        """ Текущая скорость """
        return f'{self.info()} движется вперед со скоростью {self.speed}'

    def go(self, speed: int) -> str:
        """ Движение вперед """
        if speed == 0:
            return 'Вы не можете ехать с нулевой скоростью.'
        self.speed = speed
        return self.show_speed()

    def stop(self) -> str:
        """ Остановка """
        self.speed = 0
        return f'{self.info()} останавливается'

    def turn(self, direction: str) -> str:
        """ Поворот """
        match direction:
            case 'r' | 'п':
                return f'{self.info()} поворачивает направо'
            case 'l' | 'л':
                return f'{self.info()} поворачивает налево'
            case _:
                return 'Неизвестное направление'


class TownCar(Car):
    """ Лимузин """
    __speed_limit: int = 60

    def show_speed(self) -> None:
        """ Текущая скорость с предупреждением"""
        warning = '' if self.speed < self.__speed_limit else ' Превышение скорости!!!'
        return super().show_speed() + warning


class WorkCar(Car):
    """ Рабочий транспорт """
    __speed_limit: int = 40

    def show_speed(self) -> None:
        """ Текущая скорость с предупреждением"""
        warning = '' if self.speed < self.__speed_limit else ' Превышение скорости!!!'
        return super().show_speed() + warning


class SportCar(Car):
    """ Спортивный автомобиль """
    transmission: str

    def __init__(self, name: str, color: str, transmission: str = 'manual', speed: int = 0,
                 is_police: bool = False) -> None:
        super().__init__(name, color, speed, is_police)
        self.transmission = transmission


class PoliceCar(Car):
    """ Полицейский автомобиль """
    flashing_light: bool

    def __init__(self, name: str, color: str, speed: int = 0, flashing_light: bool = False) -> None:
        super().__init__(name, color, speed, is_police=True)
        self.flashing_light = flashing_light


def main():
    ''' Main body '''
    cars = [TownCar('Ford Excursion', 'Белый'),
        WorkCar('Автоцистерна', 'Оранжевая', speed=20),
        SportCar('Bugatti Veyron', 'Черный', transmission='Robot'),
        PoliceCar('Лада Калина', 'Белая', flashing_light=True)]

    for car in cars:
        if car.is_police:
            print(f'{car.color} {car.name} - это полицейский автомобиль!')
        print(car.go(20))
        print(car.turn('r'))
        print(car.go(50))
        print(car.turn('л'))
        print(car.go(80))
        print(car.stop())

if __name__ == '__main__':
    main()
