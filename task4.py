class Car:
    def __init__(self, car_speed, car_color, car_name, car_is_police):
        self.speed = car_speed
        self.color = car_color
        self.name = car_name
        self.is_police = car_is_police

    def go(self):
        return print('Car is moving...')

    def stop(self):
        return print('Car stopped...')

    def turn(self, direction):
        return print(f'Car turn {direction}')

    def show_speed(self):
        return print(f'Car`s speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning! You have exceeded your driving speed!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Warning! You have exceeded your driving speed!')


class PoliceCar(Car):
    pass


town = TownCar(45, 'Blue', 'Toyota', False)
sport = SportCar(80, 'Red', 'Ferrari', False)
work = WorkCar(50, 'Black', 'Ford', False)
police = PoliceCar(30, 'White-Blue', 'Chevrolet', True)

town.show_speed()
sport.show_speed()
work.show_speed()
police.show_speed()

print(police.color)
work.go()

town.go()
town.stop()
town.turn('right')
