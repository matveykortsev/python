with open('task2.txt', 'r') as f:
    line_counter = 0
    for index, line in enumerate(f, start=1):
        lines = line.split()
        words = len(line.split())
        line_counter += 1
        print(f'Line {index} words in line: {words}')
    print(f'Total lines {line_counter}')
