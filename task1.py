def division(x, y):
    return x/y


x = int(input('Type x: '))
y = int(input('Type y: '))

try:
    division(x, y)
except ZeroDivisionError:
    print('ZeroDivision Error, try again')