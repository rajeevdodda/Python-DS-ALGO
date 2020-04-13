def min_swaps(array):
    i = 0
    first_one = 0
    while i < len(array):
        if array[i] == 1:
            first_one = i
            break
        i += 1

    one_count = 0
    swaps = 0
    while first_one < len(array):
        if array[first_one] == 1:
            one_count += 1
        else:
            swaps += one_count
        first_one += 1

    print(swaps)


min_swaps([0, 0, 1, 0, 1, 0, 1, 1])
min_swaps([0, 1, 0, 1, 0])
