'''
# @Date    : 2022-06-19
# @Author  : Maksim Soloviov
# @Version : 1.0.0

Practical task 6 for lesson 3
6. Реализовать функцию int_func(), принимающую слова из маленьких
латинских букв и возвращающую их же, но с прописной первой буквой.
Например, print(int_func("text")) -> Text.
'''
def int_func(string: str):  # sourcery skip: use-next
    """
    Капитализация слова.
    Ограничение - только маленькие латинские буквы

    Args:
        string (str): Исходное слово

    Returns:
        str: Слово с заглавной буквы
        None: Если слово некорректно.
    """
    for char in list(string):  # Проверка на маленькие латинские
        if ord(char) not in range(97, 123):
            return None
    return string.capitalize()


def main():
    ''' Main body '''
    user_str = input('Введите слово маленькими латинскими буквами: ')
    user_str = int_func(user_str)
    if user_str is None:
        print("Некорректная строка, только маленькие латинские буквы!")
    else:
        print(user_str)


if __name__ == '__main__':
    main()
