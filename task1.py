from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self, traffic_light_color):
        self.__color = traffic_light_color

    def running(self):
        for color in cycle(self.__color):
            print(color)
            if color == 'Красный':
                sleep(7)
            elif color == 'Желтный':
                sleep(2)
            elif color == 'Зеленый':
                sleep(4)


traffic_light_colors = ['Красный', 'Желтый', 'Зеленый']
traffic_light = TrafficLight(traffic_light_colors)
traffic_light.running()
