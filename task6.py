def parse_digit(value):
    try:
        return int(value.split('(')[0])
    except ValueError:
        return 0


with open('task6.txt', 'r') as f:
    result_dict = {}
    for line in f:
        lines = line.split()
        subject = lines[0]
        hours = lines[1:]
        sum_of_hours = sum(map(parse_digit, hours))
        # sum_of_hours = sum(int(el.split('(')[0]) for el in hours)
        result_dict.update({subject: sum_of_hours})
    print(result_dict)