def maximum_weighted_probability(array_1, array_2):
    array_1_max = array_1[0]
    array_1_max_count = 1
    for i in array_1[1:]:
        if array_1_max < i:
            array_1_max = i
            array_1_max_count = 1
        elif array_1_max == i:
            array_1_max_count += 1

    array_2_max = array_2[0]
    array_2_max_count = 1
    for i in array_2[1:]:
        if array_2_max < i:
            array_2_max = i
            array_2_max_count = 1
        elif array_2_max == i:
            array_2_max_count += 1

    print((array_1_max_count * array_2_max_count) / (len(array_2) * len(array_1)))


maximum_weighted_probability([1, 2, 3], [3, 3, 3])
