# Example 2-14. A riddle

t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except TypeError as error:
    print(error)
    print(t)