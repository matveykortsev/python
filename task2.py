first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [j for i, j in zip(first_list, first_list[1:]) if j > i]

print(new_list)