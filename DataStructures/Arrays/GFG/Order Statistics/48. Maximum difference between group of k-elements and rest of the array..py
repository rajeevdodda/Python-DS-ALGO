def max_difference(array: list, k):
    array.sort()

    print(max(abs(sum(array) - 2 * sum(array[0:k])), abs(sum(array) - 2 * sum(array[-k:]))))
    pass


max_difference([1, 5, 2, 6, 3], 2)
max_difference([1, -1, 3, -2, -3], 2)
max_difference([1, 7, 4, 8, -1, 5, 2, 1], 3)