# Определение времени года

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
seasons = dict(зима = {12, 1, 2}, весна = {3, 4, 5}, лето = {6, 7, 8}, осень={9, 10, 11})
month = int(input('Введите месяц в виде целого числа (1-12): '))
for season, season_months in seasons.items():
    if month in season_months:
        break
print(f'Если {months[month - 1]},то время года — {season}!')