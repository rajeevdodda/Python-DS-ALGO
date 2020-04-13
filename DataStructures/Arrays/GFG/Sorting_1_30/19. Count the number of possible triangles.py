from DataStructures.Arrays.GFG.Sorting.merge_sort import merge_sort


def number_of_triangles(array: list):
    count = 0
    merge_sort(array)
    for i in range(len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            k = j + 1
            while k < len(array) and array[i] + array[j] > array[k]:
                k += 1
                count += 1

    print(count)


number_of_triangles([4, 6, 3, 7])
number_of_triangles([10, 21, 22, 100, 101, 200, 300])
