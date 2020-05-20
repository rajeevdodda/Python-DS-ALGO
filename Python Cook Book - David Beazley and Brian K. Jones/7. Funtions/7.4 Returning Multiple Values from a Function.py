def my_func(a, b, c):
    # tuple will be returned
    return a, b, c


t = my_func(1, 2, 3)
print(type(t), t)

x, y, z = my_func(1, 2, 3)
print(x, y, z)
