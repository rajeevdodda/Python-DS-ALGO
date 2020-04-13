def minimum_product(array: list):
    first_min = min(array[0], array[1])
    second_min = max(array[0], array[1])
    for i in array[2:]:
        if first_min > i:
            first_min, second_min = i, first_min
        elif second_min > i:
            second_min = i
    print(first_min * second_min)


minimum_product([11, 8, 5, 7, 5, 100])
minimum_product(list(range(1, 10)))
