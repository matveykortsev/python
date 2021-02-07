def my_func(x, y, z):
    my_list = [x, y, z]
    return sum(sorted(my_list)[-2:])


x = int(input('Type x: '))
y = int(input('Type y: '))
z = int(input('Type z: '))

print(f'Sum of 2 max elements {x}, {y}, {z} = ', my_func(x, y, z))