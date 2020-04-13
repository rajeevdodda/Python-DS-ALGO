def product_maximum(array_1, array_2):
    array_2_min = array_2[0]

    for i in array_2[1:]:
        if i < array_2_min:
            array_2_min = i
    array_1_max = array_1[0]
    for i in array_1[1:]:
        if array_1_max < i:
            array_1_max = i

    print(array_1_max * array_2_min)


product_maximum([5, 7, 9, 3, 6, 2], [1, 2, 6, -1, 0, 9])
