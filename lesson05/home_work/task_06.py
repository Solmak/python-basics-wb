'''
@Date    : 2022-06-27
@Author  : Maksim Soloviov
Practical task 6 for lesson 5
6. Сформировать (не программно) текстовый файл. В нём каждая строка
должна описывать учебный предмет и наличие лекционных, практических и
лабораторных занятий по предмету. Сюда должно входить и количество
занятий. Необязательно, чтобы для каждого предмета были все типы
занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести его на экран.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

def info_analysis(info: str):
    '''Функция подсчета учебных часов по предмету

    Так как файл строго структурирован, не имеет смысла делать
    синтаксический анализ. Просто убираем служебные символы, по виду
    учебных часов. В случае изменения, просто редактируем список
    служебных символов. Как вариант, срез по скобку.

    Args:
        info (str): Строка информации о предмете вида:
                                '100(л) 50(пр) 20(лаб)'

    Returns:
        int: Общее количество часов по предмету
    '''

    service_symbols = ['-', '(л)', '(пр)', '(лаб)']

    for symbol in service_symbols:
        info = info.replace(symbol, '')
    info = [int(x) for x in info.split()]

    return sum(info)



def main():
    ''' Main body '''
    # Формируем словарь учебных предметов из файла
    edu_classes = {}
    with open('task_06.txt', 'r', encoding='utf-8') as user_file:
        for line in user_file.readlines():
            subj, info = line.split(':')
            edu_classes[subj] = info_analysis(info)


    print('Исходный файл:')
    with open('task_06.txt', 'r', encoding='utf-8') as user_file:
        print(user_file.read())

    print('\nСформированный словарь:')
    print(edu_classes)

if __name__ == '__main__':
    main()
    