def selection_sort(array):
    swaps_increasing = 0
    for i in range(len(array)):
        minimum = array[i]
        minimum_index = i
        for j in range(i + 1, len(array)):
            if array[j] < minimum:
                minimum = array[j]
                minimum_index = j

        if array[i] > minimum:
            array[i], array[minimum_index] = array[minimum_index], array[i]
            swaps_increasing += 1
    print(array)

    swaps_decreasing = 0
    for i in range(len(array)):
        minimum = array[i]
        minimum_index = i
        for j in range(i + 1, len(array)):
            if array[j] > minimum:
                minimum = array[j]
                minimum_index = j

        if array[i] > minimum:
            array[i], array[minimum_index] = array[minimum_index], array[i]
            swaps_decreasing += 1

    print(array)
    print(min(swaps_decreasing, swaps_increasing))


selection_sort([1, 5, 4, 3, 2])
selection_sort(list(range(10, -1, -1)))
