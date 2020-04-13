def maximize_elements(array1: list, array2: list):
    array1.sort(reverse=True)
    array2.sort(reverse=True)
    print(array1, array2)
    i = 0
    j = 0
    k = 0
    new_array = list()
    # while i < len(array1) and j < len(array2) k:
    while k < len(array1):
        k += 1
        if array1[i] < array2[j]:
            new_array.append(array2[j])
            j += 1
        elif array1[i] > array2[j]:
            new_array.append(array1[i])
            i += 1
        elif array1[i] == array2[j]:
            new_array.append(array2[j])
            j += 1
            i += 1
    print(new_array)


maximize_elements([7, 4, 8, 0, 1], [9, 7, 2, 3, 6])
