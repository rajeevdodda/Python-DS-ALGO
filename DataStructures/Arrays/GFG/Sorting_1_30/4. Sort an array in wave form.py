def sort_wave_form(array: list):
    array.sort()
    i = 0
    while i < len(array) - 1:
        array[i], array[i + 1] = array[i + 1], array[i]
        i += 2
    print(array)


def sort_wave_form2(array: list):
    for i in range(0, len(array), 2):
        # if current element is smaller than the next element then swap 2 elements.

        if i > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]

        # if current element is smaller than the next element.
        if i < len(array) - 1 and array[i] < array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    print(array)


if __name__ == '__main__':
    sort_wave_form(list(range(10)))
    sort_wave_form2([10, 5, 6, 3, 2, 20, 100, 80])
