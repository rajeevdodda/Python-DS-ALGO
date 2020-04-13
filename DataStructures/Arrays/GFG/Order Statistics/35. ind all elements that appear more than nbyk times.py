def more_than_n_by_k(array, k):
    n = len(array)
    sample_dict = dict()
    for i in array:
        sample_dict[i] = sample_dict.get(i, 0) + 1

    for key, val in sample_dict.items():
        if val >= n / k:
            print("number : ", key, " value :", val)


more_than_n_by_k([4, 5, 6, 7, 8, 4, 4], 3)
