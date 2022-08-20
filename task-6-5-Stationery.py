# Stationery

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки ({self.title})')
        print(self.title, 'в деле\n')

class Pencil(Stationery):

    def draw(self):
        print(f'{self.title}.', end=' ')
        super().draw()
        print('Рисуем карандашом\n')

class Handle(Stationery):

    def draw(self):
        print(self.title)
        print('Отрисовка невозможна, маркер высох\n')

pen_1 = Pen('Синяя ручка')
pen_1.draw()
pencil_1 = Pencil('Красный карандашик')
pencil_1.draw()
handle_1 = Handle('Сухой маркер')
handle_1.draw()
