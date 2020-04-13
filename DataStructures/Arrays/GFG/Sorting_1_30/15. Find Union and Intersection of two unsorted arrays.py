from DataStructures.Arrays.GFG.Sorting.merge_sort import merge_sort


def union_intersection_unsorted(array_1, array_2):
    merge_sort(array_1)
    merge_sort(array_2)

    array_union = list()
    array_intersection = list()
    i, j = 0, 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] > array_2[j]:
            array_union.append(array_2[j])
            j += 1
        elif array_1[i] < array_2[j]:
            array_union.append(array_1[i])
            i += 1
        else:
            array_union.append(array_1[i])
            array_intersection.append(array_1[i])
            i += 1
            j += 1
    while i < len(array_1):
        array_union.append(array_1[i])
        i += 1
    while j < len(array_2):
        array_union.append(array_2[j])
        j += 1

    print(array_union)
    print(array_intersection)


union_intersection_unsorted([7, 1, 5, 2, 3, 6], [3, 8, 6, 20, 7])
