'''
@Date    : 2022-06-26
@Author  : Maksim Soloviov
Practical task 3 for lesson 5
3. Создать текстовый файл (не программно). Построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто
из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих
сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''


def main():
    ''' Main body '''
    salaries = []
    print('Список сотрудников с зарплатой менее 20 000:')
    with open('task_03.txt', encoding='utf-8') as user_file:
        for line in user_file.readlines():
            surname, salary = line.split()
            salary = float(salary)
            salaries.append(salary)
            if salary < 20000:
                print(surname)

    print(
        f'\nСредняя  величина дохода: {sum(salaries) / len(salaries):.2f}'
    )


if __name__ == '__main__':
    main()
