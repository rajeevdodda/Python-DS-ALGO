def construct_pair_sum(pair_array: list, n):
    array = [None] * n
    array[0] = (pair_array[0] + pair_array[1] - pair_array[n - 1]) // 2
    for i in range(1, n):
        array[i] = pair_array[i-1] - array[0]
    print(array)


construct_pair_sum([14, 9, 10, 11, 12, 7], 4)
