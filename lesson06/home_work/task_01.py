'''
@Date    : 2022-07-03
@Author  : Maksim Soloviov
Practical task 1 for lesson 6

1. Создать класс TrafficLight (светофор).
Определить у него один атрибут color (цвет) и метод running (запуск);
Атрибут реализовать как приватный; в рамках метода реализовать
переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
Переключение между режимами должно осуществляться только в указанном
порядке (красный, жёлтый, зелёный);
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
import threading
from time import sleep
from itertools import cycle


class TrafficLight:
    """Светофор

    Класс сфетофора, осуществляет циклическое переключение цветов
    """
    __color: str

    def __init__(self) -> None:
        self.__color = 'green'

    def running(self) -> None:
        ''' Работа светофора '''
        while True:
            self.__color = 'red'
            print(self.__color)
            sleep(7)
            self.__color = 'yellow'
            print(self.__color)
            sleep(2)
            self.__color = 'green'
            print(self.__color)
            sleep(12)


class NewTrafficLight:
    """ Усложненный Светофор
    Класс сфетофора, осуществляет циклическое переключение цветов
    Первый непонравился, надо словарь. Работа потоком
    """
    __color: str
    __mode: dict = {}

    def __init__(self, red: int = 7, yellow: int = 2, green: int = 12) -> None:
        self.__color = 'green'
        self.__mode['red'] = red
        self.__mode['yellow'] = yellow
        self.__mode['green'] = green

    def running(self, arg) -> None:
        ''' Работа светофора '''
        # Вариает с цикличным словарем
        for color, time in cycle(self.__mode.items()):
            if arg['stop']:
                break
            self.__color = color
            print(self.__color)
            threading.Event().wait(time)
            if self.__color != color:
                print('The traffic light is faulty!')
                break


def main():
    ''' Main body '''
    tl1 = TrafficLight()
    try:
        print("To turn off traffic light, press Ctrl-C")
        tl1.running()
    except KeyboardInterrupt:
        print('Turn off traffic light')
    input('Press Enter...')

    # Работа нового
    is_running = {"stop": False}
    tl2 = NewTrafficLight()
    tl2_thread = threading.Thread(target=tl2.running, args=(is_running, ))
    tl2_thread.start()

    while True:
        try:
            sleep(0.5)
        except KeyboardInterrupt:
            is_running['stop'] = True
            print(
                'Turning off traffic light. Wait for the end of the cycle...')
            break

    tl2_thread.join()

    input('Press Enter...')

    # Тест проверок нового
    is_running = {"stop": False}
    tl2 = NewTrafficLight()
    tl2_thread = threading.Thread(target=tl2.running, args=(is_running, ))
    tl2_thread.start()

    tl2._NewTrafficLight__color = input(
        'Any text -> new traffic light color (fault test): ')
    print('Wait for the end of the cycle...')

    tl2_thread.join()


if __name__ == '__main__':
    main()
