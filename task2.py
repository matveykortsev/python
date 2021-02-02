number_to_convert = int(input('Введите время в секундах '))

hours = number_to_convert // 3600
delta = number_to_convert % 3600
minutes = delta // 60
seconds = delta % 60

print('{0}:{1}:{2}' .format(hours, minutes, seconds))