def median_mean(array: list):
    n = len(array)
    print("mean :", sum(array) / n)
    array.sort()
    print(array)
    if n % 2 == 0:
        median = array[int((n / 2) - 1)] + array[int(n / 2)]
    else:
        median = array[int(n / 2) - 1]
    print(n, median)


median_mean([1, 3, 4, 2, 6, 5, 8, 7])
median_mean([1, 3, 4, 2, 6, 5, 8])