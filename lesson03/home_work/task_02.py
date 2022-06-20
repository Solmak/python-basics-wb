'''
# @Date    : 2022-06-19
# @Author  : Maksim Soloviov
# @Version : 1.0.0

Practical task 2 for lesson 3
2. Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город
проживания, email, телефон. Функция должна принимать параметры как
именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
'''


def print_user_info(name, surname, birth_year, domicile, email, phone):
    """Вывод данных о личности
    Args:
        name (str): Имя
        surname (str): Фамилия
        birth_year (str or int): Год рождения
        domicile (str): Место проживания
        email (str): Email
        phone (str): Телефон
    """
    # Чтобы уместиться
    result = " ".join([
        f"{surname} {name}: Год рождения: {birth_year},",
        f"Место проживания: {domicile}, Email: {email}, Телефон: {phone}"
    ])
    print(result)
    return result


def main():
    ''' Main body '''
    # Не будем напрягать пользователя, введем сами
    print_user_info(
        name="Василий",
        surname="Пупкин",
        birth_year="2001",
        domicile="Забугорское",
        email="v.pupkin@chtoto.ru",
        phone="+7 (980) 123-45-67",
    )


if __name__ == '__main__':
    main()
