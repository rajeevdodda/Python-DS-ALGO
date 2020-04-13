def segregate_0_1(array):
    i, j = 0, len(array) - 1

    # Dutch National Flag problem
    while i < j:
        if array[i] == 0:
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
            j -= 1
    print(array)


def segregate_0_1_V2(array):
    i, j = 0, len(array) - 1

    while i < j:
        while array[i] == 0 and i < j:
            i += 1
        while array[j] == 1 and i < j:
            j -= 1
        if i < j:
            array[i], array[j] = 0, 1
            i += 1
            j -= 1
    print(array)


segregate_0_1([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])
segregate_0_1([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

print("*" * 30)

segregate_0_1_V2([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])
segregate_0_1_V2([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
