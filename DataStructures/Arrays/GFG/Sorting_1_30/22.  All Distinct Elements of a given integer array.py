def distinct_elements(array):
    sample_set = set()
    for i in array:
        if i not in sample_set:
            sample_set.add(i)

    for i in sample_set:
        print(i, end=" ")


distinct_elements([10, 0, 5, 3, 4, 3, 5, 6, 1])
