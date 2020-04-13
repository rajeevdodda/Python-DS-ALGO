def nearly_sorted_array(array: list):
    # right hand should start from index 1.
    for i in range(1, len(array)):
        # assign the value to key for comparision.
        key = array[i]

        # left hand should start iteration from highest card in left hand.
        j = i - 1

        # compare key with every value in left index until left hand gets exhausted.
        while j >= 0 and key < array[j]:
            # if key is less than value in left hand then shift the value to right.
            array[j + 1] = array[j]
            # decrement left index
            j = j - 1
        # if j goes -1 or key is greater than value it break out of the loop.
        array[j + 1] = key
    print(array)


if __name__ == '__main__':
    sample_array = [6, 5, 3, 2, 8, 10, 9]
    nearly_sorted_array(sample_array)
