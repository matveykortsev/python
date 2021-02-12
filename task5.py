from functools import reduce


def multi(prev_el, el):
    return prev_el * el


first_list = [el for el in range(100, 1001)]

print(reduce(multi, first_list))