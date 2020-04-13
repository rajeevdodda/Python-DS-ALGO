from DataStructures.Arrays.GFG.Sorting.merge_sort import merge_sort


def distinct_pairs(array, x):
    sample_dict = set()
    count = 0

    for i in range(len(array)):
        if array[i] not in sample_dict:
            sample_dict.add(array[i])

    for i in sample_dict:
        if x + i in sample_dict:
            count += 1
    print(count)


distinct_pairs([1, 1, 5, 3, 4, 2, 5], 3)
