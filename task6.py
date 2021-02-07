def int_func(words):
    return ' '.join([word.capitalize() for word in words])


words = input('Type words: ').split()
print(int_func(words))


