'''
@Date    : 2022-06-27
@Author  : Maksim Soloviov
Practical task 4 for lesson 5
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

import csv
import yaml

def main():
    ''' Main body '''
    result_lines = []
    with open('task_04_1.txt', encoding='utf-8') as user_file:
        # Посмотрел я на это перед сдачей... Надо было конечно изящней и
        # универсальней, со словарем. Но не стал переделывать. Жарко...
        # И на дачу пора ехать :)
        for line in user_file.readlines():
            numeral, digital = line.split(' - ')
            match numeral:
                case 'One':
                    numeral = 'Один'
                case 'Two':
                    numeral = 'Два'
                case 'Three':
                    numeral = 'Три'
                case 'Four':
                    numeral = 'Четыре'
            result_lines.append(f'{numeral} - {digital}')


    with open('task_04_2.txt', 'w', encoding='utf-8') as user_file:
        user_file.writelines(result_lines)

# Вспомнил про csv и yaml. Решил добавить сюда
    # csv
    result_list = [line.strip().split(' - ') for line in result_lines]
    with open('task_04_2.csv', 'w',newline='', encoding='utf-8') as csv_file:
        csv_wr = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_wr.writerows(result_list)
    # yaml
    result_dict = {num: int(dgt) for num, dgt in result_list}
    with open('task_04_2.yaml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(result_dict,yaml_file, allow_unicode=True )

    print('Новый txt файл:')
    with open('task_04_2.txt', encoding='utf-8') as user_file:
        print(user_file.read())
    print('Новый csv файл:')
    with open('task_04_2.csv', encoding='utf-8') as user_file:
        print(user_file.read())
    print('Новый yaml файл:')
    with open('task_04_2.yaml', encoding='utf-8') as user_file:
        print(user_file.read())

if __name__ == '__main__':
    main()
