# Дата


class Date:

    ds_by_ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def valid_date(obj):
        day, month = obj.day, obj.month
        month %= 12
        month = 12 if not month else month
        day %= Date.ds_by_ms[month - 1]
        day = Date.ds_by_ms[month - 1] if not day else day
        if (day, month) != (obj.day, obj.month):
            print('Некорректная дата была исправлена')
            obj.day, obj.month = day, month
        else:
            print('Дата корректная')

    @classmethod
    def set_date(cls, dmy):
        day, month, year = map(int, dmy.split('-'))
        return  cls(day, month, year)


first_date = Date.set_date('28-12-2005')
print(first_date.day)
print(first_date.month)
print(first_date.year)
Date.valid_date(first_date)
print()
second_date = Date.set_date('32-13-2005')
print(second_date.day)
print(second_date.month)
print(second_date.year)
Date.valid_date(second_date)
print(second_date.day)
print(second_date.month)
print(second_date.year)
