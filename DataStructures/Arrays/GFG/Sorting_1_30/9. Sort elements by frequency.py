def sort_array(array: list):
    sample_dict = dict()

    for i in range(len(array)):
        if array[i] not in sample_dict.keys():
            sample_dict[array[i]] = [array[i], i, 1]
        else:
            sample_dict[array[i]][2] += 1
    array = sorted(sample_dict.values(), key=lambda element: (element[2], len(array) - element[1]), reverse=True)
    for i in array:
        j = 0
        while j < i[2]:
            print(i[0], end=" ")
            j += 1


if __name__ == "__main__":
    sort_array([2, 5, 2, 8, 5, 6, 8, 8])
