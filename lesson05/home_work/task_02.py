'''
@Date    : 2022-06-26
@Author  : Maksim Soloviov
Practical task 2 for lesson 5
2. Создать текстовый файл (не программно), сохранить в нём несколько
строк, выполнить подсчёт строк и слов в каждой строке.
'''


def main():
    ''' Main body '''
    file_stat: list
    with open('task_02.txt', encoding='utf-8') as user_file:
        file_stat = [len(line.split()) for line in user_file.readlines()]

    print('Статистика файла:')
    print(
        f'Количество строк: {len(file_stat)}. Количество слов: {sum(file_stat)}'
    )

    for line, words in enumerate(file_stat, 1):
        print(f'Строка {line}: Слов: {words}')


if __name__ == '__main__':
    main()
