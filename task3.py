seasons_list = [
    'Winter',
    'Winter',
    'Winter',
    'Spring',
    'Spring',
    'Spring',
    'Summer',
    'Autumn',
    'Autumn',
    'Autumn'
]
pick_month = int(input('Type month number: '))
print(seasons_list[pick_month+1])


seasons_dict = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter',
}

pick_month = int(input('Type month number: '))
print(seasons_dict[pick_month])