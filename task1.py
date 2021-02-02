from sys import argv


def salary(hours, hourly_rate, bonus):
    return (hours * hourly_rate) + bonus


hours = int(argv[1])
hourly_rate = int(argv[2])
bonus = int(argv[3])

print(salary(hours, hourly_rate, bonus))
