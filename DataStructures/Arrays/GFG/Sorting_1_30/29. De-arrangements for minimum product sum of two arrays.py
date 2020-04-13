def de_arrangements_product_sum(array1, array2):
    array1_decreasing = sorted(array1, reverse=True)
    array2_increasing = sorted(array2)
    array1_decreasing_count = 0
    array2_increasing_count = 0

    array1_increasing = sorted(array1)
    array2_decreasing = sorted(array2, reverse=True)
    array1_increasing_count = 0
    array2_decreasing_count = 0

    for i in range(len(array1)):
        if array1[i] != array1_decreasing[i]:
            array1_decreasing_count += 1
        if array2[i] != array2_increasing[i]:
            array2_increasing_count += 1

        if array1[i] != array1_increasing[i]:
            array1_increasing_count += 1
        if array2[i] != array2_decreasing[i]:
            array2_decreasing_count += 1
   

    print(min((array1_decreasing_count + array2_increasing_count), (array1_increasing_count+array2_decreasing_count)))


de_arrangements_product_sum([1, 2, 3, 4], [6, 3, 4, 5])
