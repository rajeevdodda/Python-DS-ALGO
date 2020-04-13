def sort012(array: list):
    low, mid, high = 0, 0, len(array) - 1

    while mid <= high:
        if array[mid] == 1:
            mid += 1
        elif array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        else:
            array[high], array[mid] = array[mid], array[high]
            high -= 1

    print(array)


sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
