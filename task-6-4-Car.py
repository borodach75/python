# Car

from random import choice

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'поехала')

    def stop(self):
        print(self.name, 'остановилась')

    def turn(self, direction):
        print(self.name, 'повернула', direction)

    def random_turn(self):
        self.turn(choice(('направо', 'налево')))

    def show_speed(self):
        print('Скорость', self.__class__.__name__, self.name, self.speed)
        if self.is_police:
            print('Для полицейского скорость нормальная')

class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Для городского автомобиля скорость превышена!')

class SportCar(Car):

    pass

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Для рабочего автомобиля скорость превышена!')

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car_1 = TownCar(65, 'Синий', 'Ford Focus')
car_2 = SportCar(120, 'Красный', 'Lamborghini Aventador')
car_3 = WorkCar(55, 'Зелёный', 'Лада Ларгус')
car_4 = PoliceCar(80, 'Белый', 'Chevrolet Cruze')

print(f'\n{car_1.name = }, {car_1.color = }')
car_1.show_speed()
print(f'\n{car_2.name = }, {car_2.color = }')
car_2.show_speed()
print(f'\n{car_3.name = }, {car_3.color = }')
car_3.show_speed()
print(f'\n{car_4.name = }, {car_4.color = }')
car_4.show_speed()

print()
car_2.go()
car_3.go()
car_2.stop()
car_4.go()
car_3.turn('налево')
car_1.go()
car_4.random_turn()
car_1.turn('направо')
car_1.random_turn()

print()
if car_4.is_police:
    print(car_4.name, '— полицейская машина!')
