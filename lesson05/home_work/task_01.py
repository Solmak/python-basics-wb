'''
@Date    : 2022-06-26
@Author  : Maksim Soloviov
Practical task 1 for lesson 5
1. Создать программный файл в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных
будет свидетельствовать пустая строка.
'''

def main():
    ''' Main body '''
    # Можно открывать и внутри цикла с дозаписью. Но хоть и минимизируем
    # время открытого, но не чистим при старте. В общем сделал так.
    with open('task_01.txt', 'w', encoding='utf-8') as user_file:
        user_input = ' '
        while user_input:
            user_input = input('Введите строку: ')
            user_file.write(user_input + '\n')

    print('\nВы ввели следующий текст:')
    with open('task_01.txt', encoding='utf-8') as user_file:
        print(user_file.read())

if __name__ == '__main__':
    main()
