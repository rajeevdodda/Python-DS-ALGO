def pair_sum(array: list):
    max1 = max2 = float('-inf')
    for i in array:
        if i > max1:
            max1, max2 = i, max1
        elif i > max2:
            max2 = i
    print(max1 + max2)


pair_sum([12, 34, 10, 6, 40])
