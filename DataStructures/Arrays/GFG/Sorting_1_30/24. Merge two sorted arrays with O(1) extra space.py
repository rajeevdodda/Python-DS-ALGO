def merge_two_sorted_array(array_1, array_2):
    i = 0
    while i < len(array_1):
        j = 0

        if array_1[i] > array_2[j]:
            array_1[i], array_2[j] = array_2[j], array_1[i]
            j += 1
            while j < len(array_2):
                if array_2[j] < array_2[j - 1]:
                    array_2[j], array_2[j - 1] = array_2[j - 1], array_2[j]
                    j += 1
                else:
                    break

        i += 1
    print(array_1, array_2)


merge_two_sorted_array([1, 5, 9, 10, 15, 20], [2, 3, 8, 13])
