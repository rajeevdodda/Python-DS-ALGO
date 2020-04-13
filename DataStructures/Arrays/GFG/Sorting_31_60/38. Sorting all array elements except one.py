def sort_except_one(arrray, k):
    new_array = sorted(arrray[0:k] + arrray[k + 1:])
    print()
    i = 0
    while i < len(arrray) - 1:
        if i == k:
            i += 1
            continue
        else:
            arrray[i] = new_array[i]
        i += 1
    print(arrray)


# sort_except_one([10, 4, 11, 7, 6, 20], 2)


def sort_except_negative(array):
    print(array)
    new_array = [i for i in array if i > 0]
    new_array.sort()
    print(new_array)
    i, j = 0, 0
    while i < len(array):
        if array[i] < 0:
            i += 1
        else:
            array[i] = new_array[j]
            i += 1
            j += 1
    print(array)



sort_except_negative([5, 6, -1, 10, 2, -6])
