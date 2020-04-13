def merge_m_n(array_m: list, array_n: list):
    j = len(array_m) - 1
    for i in range(len(array_m) - 1, -1, -1):
        if array_m[i] != "NA":
            array_m[j] = array_m[i]
            j -= 1
    j += 1
    i = 0
    k = 0
    while k < len(array_m):
        if array_m[j] <= array_n[i]:
            array_m[k] = array_m[j]
            j += 1
            k += 1
            if j == len(array_m):
                break

        else:
            array_m[k] = array_n[i]
            i += 1
            k += 1
            if i == len(array_n):
                break

    if j == len(array_m):
        while i < len(array_n):
            array_m[k] = array_n[i]
            k += 1
            i += 1

    if i == len(array_n):
        while j < len(array_m):
            array_m[k] = array_m[j]
            k += 1
            j += 1
    print(array_m)


if __name__ == '__main__':
    merge_m_n([2, 8, "NA", "NA", "NA", 13, "NA", 15, 20], [5, 7, 9, 25])
    pass
