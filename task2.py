class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self):
        return self._length * self._width * 25 * 5


road = Road(20, 5000)
print(f'For full road coverage needed {road.calculation()} kg')