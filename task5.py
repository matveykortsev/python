with open('task5.txt', 'w+') as f:
    f.write('3 4 5 6 7 8 9 10')
    f.seek(0)
    line = f.readline().split()
    sum_of_digit = sum(map(lambda value: int(value), line))
    print(f'Sum of integers in file = {sum_of_digit}')
