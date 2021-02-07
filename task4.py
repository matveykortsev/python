def my_func_version_1(x, y):
    return x ** y


def my_func_version_2(x, y):
    multi = 1
    for i in range(0, abs(y)):
        multi *= x
    return 1/multi


print(my_func_version_1(50, -4))
print(my_func_version_2(50, -4))
