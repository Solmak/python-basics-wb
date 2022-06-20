'''
# @Date    : 2022-06-19
# @Author  : Maksim Soloviov
# @Version : 1.0.0

Practical task 7 for lesson 3
7. Продолжить работу над заданием. В программу должна попадать строка из
слов, разделённых пробелом. Каждое слово состоит из латинских букв в
нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Используйте написанную ранее
функцию int_func().
'''
from task_06 import int_func


def main():
    ''' Main body '''
    # Если не устраивает title()...
    print('Введите строку из маленьких латинских букв.',
          'Cлова разделите пробелом',
          'Или просто нажмите Enter',
          sep='\n')
    my_string = input('Ваша строка: ')

    if not my_string:
        print('Если вы ленивы, сделаем за вас...')
        my_string = 'a titlecased version of the string'

    print('Исходная:', my_string)
    my_string = my_string.split()
    my_string = map(int_func, my_string)
    my_string = " ".join(my_string)
    print('Обработанная:', my_string)


if __name__ == '__main__':
    main()
