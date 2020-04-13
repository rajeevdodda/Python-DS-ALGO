def sort_array(array_a: list, array_b: list):
    for i in range(len(array_b)):
        if array_b[i] == 1:
            if array_a[i] > array_a[i + 1]:
                array_a[i], array_a[i + 1] = array_a[i + 1], array_a[i]
    print(array_a)
    for i in range(len(array_a)):
        if array_a[i] != i + 1:
            print("Its not sorted array!")
            break
    else:
        print("sorted array")


if __name__ == "__main__":
    sort_array([1, 2, 5, 3, 4, 6], [0, 1, 1, 1, 0])
    sort_array([2, 3, 1, 4, 5, 6], [0, 1, 1, 1, 1])
