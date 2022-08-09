def user_print(**user):
    '''Вывод данных пользователя'''

    # Вариант 1
    print(f"Имя: {user['name']}, фамилия: {user['soname']}, год рождения: {user['year']},",
          f"город проживания: {user['city']}, e-mail: {user['e_mail']}, телефон: {user['tel']}")

    # Вариант 2
    user_fields = dict(name='Имя', soname='Фамилия', year='Год рождения',
                       city='Город проживания', e_mail='e-mail', tel='Телефон')
    for field, val in user_fields.items():
        print(f'{val}: {user[field]}', end='. ')

user_print(year=1957, name='Liam', soname='Nison', e_mail='LN@goto.com', tel='5-525-123-456-17', city='London')
