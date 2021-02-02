with open('task4.txt', 'r') as f:
    new_lines = []
    for line in f:
        new_line = line.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре')
        new_lines.append(new_line)
with open('task4_updated.txt', 'w+') as f_upd:
    f_upd.writelines(new_lines)