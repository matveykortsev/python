from itertools import count, cycle


for el in count(3):
    if el > 10:
        break
    else:
        print(el)

countries = ['Russia', 'USA', 'UK']
с = 0
for el in cycle(countries):
    if с > 15:
        break
    print(el)
    с += 1