'''
@Date    : 2022-06-27
@Author  : Maksim Soloviov
Practical task 5 for lesson 5
5. Создать (программно) текстовый файл, записать в него программно набор
чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел
в файле и выводить её на экран.
'''
from random import randint

def main():
    ''' Main body '''
    result_string = ''

    # Генерируем строку чисел. Можно, конечно, спросить у пользователя..
    result_string = ' '.join([str(randint(1, 100)) for _ in range(30)])
    # Строку в файл
    with open('task_05.txt', 'w', encoding='utf-8') as user_file:
        user_file.write(result_string)

    # Работа со сгенеренным файлом
    with open('task_05.txt', 'r', encoding='utf-8') as user_file:
        file_string = user_file.read()
    print(f'Содержимое файла: \n{file_string}')

    file_numbers = [int(i) for i in file_string.split()]
    print(f'Сумма чисел в файле: {sum(file_numbers)}')

if __name__ == '__main__':
    main()
    