from DataStructures.Arrays.GFG.Sorting.merge_sort import merge_sort
import sys


def minimum_abs_pair(array):
    merge_sort(array)
    i, j, absolute_minimum = 0, len(array) - 1, sys.maxsize
    min_value, max_value = None, None
    while i < j:
        minimum = array[i] + array[j]

        if absolute_minimum > abs(minimum):
            absolute_minimum = abs(minimum)
            min_value, max_value = array[i], array[j]
            if absolute_minimum == 0:
                break
        if minimum > 0:
            j -= 1
        else:
            i += 1

    return min_value, max_value


if __name__ == "__main__":
    print(minimum_abs_pair([1, 60, -1, 1, -80, 85]))
