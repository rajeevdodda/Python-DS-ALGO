from DataStructures.Arrays.GFG.Sorting.merge_sort import merge_sort
from DataStructures.Arrays.GFG.Sorting.binary_search import binarySearch


def pairs_count(array_x: list, array_y: list):
    merge_sort(array_y)
    merge_sort(array_x)
    print(array_x, array_y)
    i, j = len(array_x) - 1, 0
    count = 0
    while i < len(array_x):
        while j < len(array_y):
            if array_x[i] < array_y[j]:
                count += (i + 1)
                j += 1
                if j == len(array_y):
                    print(count)
                    break
        i -= 1
    print(count)


pairs_count([10, 19, 18], [11, 15, 9])
