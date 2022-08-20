# TrafficLight

from time import sleep
from itertools import cycle

traffic_dict = {'Red': ('\033[31m', 7), 'Yellow': ('\033[33m', 2), 'Green': ('\033[32m', 5)}

class TrafficLight:

    def running(self, iter_num):
        for color, _ in zip(cycle(traffic_dict.keys()), range(iter_num)):
            self.__color = color
            pref = traffic_dict[self.__color][0]
            print(pref, self.__color)
            sleep(traffic_dict[self.__color][1])

traffic_light_1 = TrafficLight()
traffic_light_1.running(5)          # Кол-во переключений светофора
