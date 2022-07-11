'''
@Date    : 2022-07-10
@Author  : Maksim Soloviov
Practical tasks 4-6 for lesson 8
4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым для
классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
сканер, ксерокс). В базовом классе определите параметры, общие для
приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые
отвечают за приём оргтехники на склад и передачу в определённое
подразделение компании. Для хранения данных о наименовании и количестве
единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества
принтеров, отправленных на склад, нельзя использовать строковый тип
данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''


class OfficeEquipment:
    """ Оргтехника """
    brand: str
    model: str
    size: int

    def __init__(self, brand: str, model: str, size: int = 1) -> None:
        self.brand = brand
        self.model = model
        self.size = size

    def __str__(self) -> str:
        return f'{self.brand} {self.model}'


class Printer(OfficeEquipment):
    """ Класс Принтеры """
    print_technology: str
    paper_size: str
    is_color: bool

    def __init__(self,
                 brand: str,
                 model: str,
                 size: int = 1,
                 print_technology: str = 'laser',
                 paper_size: str = 'A4',
                 is_color: bool = False) -> None:
        super().__init__(brand, model, size)
        self.print_technology = print_technology
        self.paper_size = paper_size
        self.is_color = is_color

    def __str__(self) -> str:
        return f'Принтер {super().__str__()}'


class Scanner(OfficeEquipment):
    """ Класс Сканеры """
    scanner_type: str
    original_size: str
    color_depth: int

    def __init__(
            self,
            brand: str,
            model: str,
            size: int = 1,
            scanner_type: str = 'flatbed',  # broach
            original_size: str = 'A4',
            color_depth: int = 48) -> None:
        super().__init__(brand, model, size)
        self.scanner_type = scanner_type
        self.original_size = original_size
        self.color_depth = color_depth

    def __str__(self) -> str:
        return f'Сканер {super().__str__()}'


class Copier(OfficeEquipment):
    """ Класс Копиры """
    paper_size: str
    is_color: bool
    max_resolution: tuple

    def __init__(
        self,
        brand: str,
        model: str,
        size: int = 1,
        paper_size: str = 'A4',
        is_color: bool = False,
        max_resolution: tuple = (600, 600)) -> None:
        super().__init__(brand, model, size)
        self.paper_size = paper_size
        self.is_color = is_color
        self.max_resolution = max_resolution

    def __str__(self) -> str:
        return f'Копир {super().__str__()}'


class Storage:
    """ Склад """
    title: str
    __max_capacity: int
    _content: dict

    def __init__(self, title: str, max_capacity: int) -> None:
        """ Конструктор склада"""
        self.title = title
        self._content = {}
        self.max_capacity = max_capacity

    @property
    def fullness(self) -> int:
        """ Наполненность """
        return sum(item.size * self._content[item] for item in self._content)

    @property
    def max_capacity(self):
        """ Максисмальная вместимость """
        return self.__max_capacity

    @max_capacity.setter
    def max_capacity(self, value: int):
        if value < self.fullness:
            self.__max_capacity = max(1, self.fullness)
            print(
                f'''Ошибочное значение.
Устанавливаю размер склада в минимально возможный: {self.max_capacity}'''
            )
        else:
            self.__max_capacity = value

    @property
    def free_space(self) -> int:
        """ Свободное место """
        return self.max_capacity - self.fullness

    def add(self, equipment: OfficeEquipment, count: int = 1) -> bool:
        """ Прием техники на склад """
        if equipment.size * count > self.free_space:
            print('На складе не хватает места для размещения оборудования')
            return False
        if equipment in list(self._content):
            self._content[equipment] += count
        else:
            self._content[equipment] = count

        return True

    def issuance(self, equipment: OfficeEquipment, count: int = 1) -> bool:
        """ Выдача техники со склада """
        if self._content[equipment] < count:
            print(f'{equipment} - нет требуемого количества')
            return False
        self._content[equipment] -= count
        return True

    def __str__(self) -> str:
        return ', '.join([
            f'{self.title}: Размер: {self.max_capacity}',
            f'Занято: {self.fullness}', f'Свободно: {self.free_space}'
        ])

    # def get_full_info(self):
    #     pass


def main():
    ''' Main body '''
    p1 = Printer('HP', 'LaserJet 4P')
    p2 = Printer('Canon', 'PIXMA G540', 1, 'ink', is_color=True)
    s1 = Scanner('Plustek', 'OpticSlim 2610 Plus')
    s2 = Scanner('iScan', 'портативный ручной', 1, 'manual', 'A4', 32)
    c1 = Copier('Pantum', 'BM5100FDN', max_resolution=(1200, 1200))
    c2 = Copier('XEROX', 'AltaLink C8170 TT', 2, 'A3')
    c3 = Copier('KYOCERA', 'TASKalfa 6053ci', 2, 'A3', True, (4800, 1200))

    print(p1)
    print(s2)
    print(c1)

    storage1 = Storage('Склад оргтехники ООО "Рогатов, Копытов и партнёры"',
                       120)
    storage1.add(p1, 1)
    storage1.add(p1, 3)
    storage1.add(p2, 5)
    storage1.add(s1, 2)
    storage1.add(s2)
    storage1.add(c1, 4)
    storage1.add(c2, 7)
    storage1.add(c3, 2)
    print(storage1)

    while storage1.issuance(c2):
        print(f'{c2} - осталось {storage1._content[c2]}')

    storage1.max_capacity = -1
    print(storage1)


if __name__ == '__main__':
    main()
# Хочется еще добавить, там, изменить тут, вставить свои исключения,
# но пора выезжать :)
# Пора воспользоваться каникулами и отпуском :)
