'''
@Date    : 2022-07-03
@Author  : Maksim Soloviov
Practical task 2 for lesson 6
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей
дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного
кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''


class Road:
    """ Дорога. Просто дорога """
    _length: int
    _width: int

    def __init__(self, length: int, width: int) -> None:
        '''Конструктор класса Road
        Args:
            length (int): Длина дороги в метрах
            width (int): Ширина дороги в метрах
        '''
        self._length = length
        self._width = width

    def get_pavement_weight(self, pavement_thickness: float,
                            pavement_weight: float) -> int:
        '''Расчет массы покрытия
        Считает массу покрытия заданной толщины и удельного веса
        Args:
            pavement_thickness (float): необходимая толщина покрытия
                в метрах
            pavement_specific_gravity (float): вес 1 кубического
                метра материал
        Returns:
            int: Масса необходимого материала в кг.
        '''
        return self._length * self._width * pavement_thickness * pavement_weight


def main():
    ''' Main body '''
    # Толщина покрытия в метрах (5 см)
    pvmnt_thick = 0.05

    # Вес куб. метра покрытия
    pvmnt_spec_gravity = 2500

    # Длина и ширина дороги в метрах
    road_length = 5000
    road_width = 20

    my_road = Road(road_length, road_width)

    print(
        'Для покрытия дороги требуется ',
        f'{my_road.get_pavement_weight(pvmnt_thick, pvmnt_spec_gravity)/1000} тонн материала'
    )


if __name__ == '__main__':
    main()
