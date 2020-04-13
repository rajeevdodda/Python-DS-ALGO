def sort_array(array_a: list):
    i, j = 0, len(array_a) - 1
    while True:
        while i < j:
            if array_a[i] == 0:
                i += 1
            else:
                break
        while j > i:
            if array_a[j] == 1:
                j -= 1
            else:
                break
        if i < j:
            array_a[i], array_a[j] = array_a[j], array_a[i]
        else:
            break
    print(array_a)


if __name__ == "__main__":
    sort_array([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])
    sort_array([1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1])
