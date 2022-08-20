# Road

class Road:
    mass_1_m = 25  # кг
    thickness = 5  # см

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def total_mass(self):
        return self._length * self._width * self.mass_1_m * self.thickness // 1000

road_1 = Road(20, 5000)  # Новый экземпляр дороги, его длина и ширина в метрах
print(f'{road_1._length} м * {road_1._width} м * {Road.mass_1_m} кг * {Road.thickness} см = {road_1.total_mass()} т')
