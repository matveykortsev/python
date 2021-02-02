with open('task1.txt', 'w') as f_obj:
    while True:
        string_to_write = input('Type string to write: ')
        f_obj.write(f'{string_to_write}\n')
        if string_to_write == '':
            break
