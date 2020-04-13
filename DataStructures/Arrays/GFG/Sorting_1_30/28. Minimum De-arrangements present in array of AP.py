def de_arrangements(array):
    a = b = array[0]
    for i in array:
        if a > i:
            a = i
        if b < i:
            b = i
    d = int((b - a) / (len(array) - 1))
    increasing = 0
    decreasing = 0
    for i in array:
        if a != i:
            increasing += 1
        if b != i:
            decreasing += 1
        a += d
        b -= d

    print(min(increasing, decreasing))


de_arrangements([8, 6, 10, 4, 2])
de_arrangements([5, 10, 15, 25, 20])
