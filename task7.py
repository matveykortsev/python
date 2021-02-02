import json


def get_profit(value):
    return value if value > 0 else 0


profits = []
firms = []
line_counter = 0
result_list = []

with open('task7.txt', 'r') as f:
    for line in f:
        lines = line.split()
        earnings = int(lines[2])
        costs = int(lines[3])
        firm = lines[0]
        profit = earnings - costs
        profits.append(profit)
        firms.append(firm)
        line_counter += 1

avg_profit = sum(map(get_profit, profits)) / line_counter
result_list.append(dict(zip(firms, profits)))
result_list.append({'average_profit': avg_profit})

with open('task7_json.txt', 'w') as f_json:
    json.dump(result_list, f_json)
