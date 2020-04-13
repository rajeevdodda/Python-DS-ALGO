def closest_pair(array1, array2, x):
    difference = float('inf')
    i = 0
    j = len(array2) - 1
    a1 = a2 = 0

    while i < len(array1) and j >= 0:
        temp = abs(x - (array1[i] + array2[j]))

        if temp < difference:
            difference = temp
            a1, a2 = array1[i], array2[j]
        if array1[i] + array2[j] > x:
            j -= 1
        else:
            i += 1
    print(a1, a2)


closest_pair([1, 4, 5, 7], [10, 20, 30, 40], 50)
closest_pair([1, 4, 5, 7], [10, 20, 30, 40], 38)
