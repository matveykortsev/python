line = input('Type string: ').split()
print(line)
for i, word in enumerate(line, start=1):
    print(i, word[0:10])