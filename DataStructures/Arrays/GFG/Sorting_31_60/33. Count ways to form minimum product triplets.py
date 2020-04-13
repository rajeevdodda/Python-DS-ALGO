def triplets_product(array: list):
    array.sort()
    count = 0

    for i in array:
        if i == array[2]:
            count += 1
    if array[0] == array[2]:
        print((count - 2) * (count - 1) / 6)
    elif array[1] == array[2]:
        print((count - 1) * count / 2)
    else:
        print(count)


triplets_product([1, 1, 1, 1, 2, 3, 4])
triplets_product([1, 2, 2, 2, 3])
triplets_product([1, 1, 2, 2])
triplets_product([1, 2, 3, 3, 5])
