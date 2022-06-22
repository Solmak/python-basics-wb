'''
@Date    : 2022-06-22
@Author  : Maksim Soloviov

Practical task 3 for lesson 4
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
'''


def main():
    ''' Main body '''
    # Пусть до 240 включительно
    result_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
    print(result_list)


if __name__ == '__main__':
    main()
