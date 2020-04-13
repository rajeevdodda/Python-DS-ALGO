def sort_based_on_abs_difference(array: list, x: int):
    n = len(array)
    difference_index_array = [(abs(x - array[i]), i) for i in range(n)]
    difference_index_array.sort(key=lambda k: k[0])

    for i in difference_index_array:
        print(array[i[1]], end=' ')


if __name__ == '__main__':
    sort_based_on_abs_difference([10, 5, 3, 9, 2], 7)
    print()
    sort_based_on_abs_difference([1, 2, 3, 4, 5], 6)
