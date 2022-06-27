'''
@Date    : 2022-06-27
@Author  : Maksim Soloviov
Practical task 7 for lesson 5
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчёт средней
прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила
убытки, также добавить её в словарь (со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{'firm_1': 5000, 'firm_2': 3000, 'firm_3': 1000}, {'average_profit': 2000}]
Подсказка: использовать менеджер контекста.
'''
import json
import csv
def main():
    ''' Main body '''
    firms = {}
    profits = []
    #  Файл с запятыми в виде разделителей, чтобы названия фирм можно
    # было делать из нескольких слов
    # В текстовом файле не кодировка слетела :) Просто герератор набора
    # букв, это названия такие :)
    with open('task_07.txt', 'r', encoding='utf-8') as user_file:
    # Сначала сделал, так, потом подумал, что запятыми ж разлелил
        # for line in user_file.readlines():
        #     name, form_owner, revenue, costs = line.split(',')
        #     profit = int(revenue) - int(costs)
        # И переделал так.
        firm_reader = csv.reader(user_file)
        for row in firm_reader:
            profit = int(row[2]) - int(row[3])
            firms[row[0]] = profit
            if profit > 0:
                profits.append(profit)

    profit = {'average_profit': round(sum(profits) / len(profits), 2)}
    firms_object = [firms, profit]

    with open('task_07.json', 'w', encoding='utf-8') as user_file:
        json.dump(firms_object, user_file)

    print('Исходный файл:')
    with open('task_07.txt', 'r', encoding='utf-8') as user_file:
        print(user_file.read())

    print('Объект загруженный из json-файла:')
    with open('task_07.json', 'r', encoding='utf-8') as user_file:
        print(json.load(user_file))

if __name__ == '__main__':
    main()
    