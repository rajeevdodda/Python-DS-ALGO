def unsorted_sub_array(array: list):
    sample_array = list()
    # for i in range(1, len(array)):
    #     if array[i] - array[i - 1] <= 0:
    #         sample_array.append("+")
    #
    #     pass
    # pass
    i, j = 0, len(array) - 1
    front_index = 0
    last_index = len(array) - 1

    while i < len(array) - 1:
        if array[i] - array[i + 1] > 0:
            front_index = i
            break
        else:
            i += 1
            if i == len(array) - 1:
                print("array sorted")
                return

    while j > -1:
        if array[j] - array[j - 1] < 0:
            last_index = j + 1
            break
        else:
            j -= 1

    i, j = 0, len(array) - 1

    front_index_v2 = 0
    last_index_v2 = len(array) - 1

    while i < len(array) - 1:
        if array[i] - array[i + 1] < 0:
            front_index_v2 = i
            break
        else:
            i += 1
            if i == len(array) - 1:
                print("array sorted")
                return

    while j > -1:
        if array[j] - array[j - 1] > 0:
            last_index_v2 = j + 1
            break
        else:
            j -= 1

    if (last_index_v2 - front_index_v2) > (last_index - front_index):
        print(front_index, last_index)
    else:
        print(front_index_v2, last_index_v2)


unsorted_sub_array([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60])

unsorted_sub_array([100, 90, 80, 72, 60, 30, 25, 40, 32])

unsorted_sub_array(list(range(10)))
unsorted_sub_array(list(range(10, -1, -1)))
