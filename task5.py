def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return value


"""Можно было вместо map-функции воспользоваться генератором"""
# my_list = [int(x) if x.lstrip('-').isdecimal() else x for x in my_list]

sum_of_list = 0
while True:
    input_list = input('Type line of numbers: ').split()
    updated_list = list(map(try_to_int, input_list))
    if 'q' in updated_list:
        updated_list.remove('q')
        sum_of_list += sum(updated_list)
        print(f'Sum of integers in list: {sum_of_list}')
        break
    sum_of_list += sum(updated_list)
    print(f'Sum of integers in list: {sum_of_list}')




