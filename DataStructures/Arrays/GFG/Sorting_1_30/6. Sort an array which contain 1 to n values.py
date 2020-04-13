def sort_array(array: list):
    print(array)
    for i in range(len(array)):
        if array[i] != i + 1:
            temp = array[i]
            array[temp-1], array[i] = array[i], array[temp-1]
    print(array)


if __name__ == "__main__":
    sort_array(list(range(10, 0, -1)))
