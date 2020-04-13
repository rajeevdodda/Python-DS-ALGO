def union_intersection(array_1, array_2):
    union_set = {i for i in array_1}
    intersection_set = set()
    for i in array_2:
        if i in union_set:
            intersection_set.add(i)
        else:
            union_set.add(i)
    print(union_set)
    print(intersection_set)


def union_intersection_v2(array_1, array_2):
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


union_intersection([1, 3, 4, 5, 7], [2, 3, 5, 6])
print("*" * 40)
union_intersection_v2([1, 3, 4, 5, 7], [2, 3, 5, 6])
