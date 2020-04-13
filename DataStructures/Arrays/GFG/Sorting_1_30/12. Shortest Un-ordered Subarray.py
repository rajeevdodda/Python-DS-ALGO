def shortest_unordered_sub_array(array):
    if increasing(array) or decreasing(array):
        print(0)
    else:
        print(3)


def increasing(array):
    for i in range(1, len(array)):
        if array[i - 1] - array[i] > 0:
            return False
    return True


def decreasing(array):
    for i in range(1, len(array)):
        if array[i - 1] - array[i] < 0:
            return False
    return True


shortest_unordered_sub_array([7, 9, 10, 8, 11])
shortest_unordered_sub_array(list(range(10)))
shortest_unordered_sub_array(list(range(10, -1, -1)))
