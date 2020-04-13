def sort_distinct(array):
    array.sort()
    i = 0
    print(array[i], end=" ")
    i += 1
    while i < len(array):
        if array[i] != array[i - 1]:
            print(array[i], end=" ")
        i += 1


sort_distinct([1, 1, 1, 2, 2, 3])
