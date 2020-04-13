def minimum_increment_decrement(array1, array2):
    array1.sort()
    array2.sort()
    count = 0
    i = 0
    while i < len(array1):
        count += abs(array1[i] - array2[i])
        i += 1

    print(count)


minimum_increment_decrement([3, 1, 1], [1, 2, 2])
