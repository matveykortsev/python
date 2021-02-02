a = int(input('Type a '))
b = int(input('Type b '))
i = 1

while a < b:
    i = i+1
    a = 1.1 * a
    print(i, '-ый день: ', a)
    if a > b:
        break
print('Ответ: На {0} день спортсмен достиг результата - не менее {1} км'.format(i, b))