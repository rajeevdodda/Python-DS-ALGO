def max_sum_path(array1, array2):
    array1_sum = array2_sum = total_sum = 0
    i = j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array1_sum += array1[i]
            i += 1
        elif array1[i] > array2[j]:
            array2_sum += array2[j]
            j += 1
        elif array1[i] == array2[j]:
            array2_sum += array2[j]
            array1_sum += array1[i]
            total_sum = max(array1_sum, array2_sum)
            array1_sum = total_sum
            array2_sum = total_sum
            i += 1
            j += 1
    while i < len(array1):
        array1_sum += array1[i]
        i += 1
    while j < len(array2):
        array2_sum += array2[j]
        j += 1

    total_sum = max(array1_sum, array2_sum)

    print(total_sum)


max_sum_path([2, 3, 7, 10, 12, 15, 30, 34], [1, 5, 7, 8, 10, 15, 16, 19])
max_sum_path([2, 3, 7, 10, 12], [1, 5, 7, 8])
