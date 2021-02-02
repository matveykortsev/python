with open('task3.txt', 'r') as f:
    salary_sum = 0
    lines_counter = 0
    for lines in f:
        line = lines.split()
        salary = float(line[1])
        salary_sum += salary
        lines_counter += 1
        if salary < 20000:
            print(f'{line[0]}`s salary is less than 20000')
    avg_salary = salary_sum / lines_counter
    print(f'Average salary is {avg_salary}')
