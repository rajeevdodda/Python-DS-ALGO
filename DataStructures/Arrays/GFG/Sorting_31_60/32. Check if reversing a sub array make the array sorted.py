def reverse_sub_array(array: list):
    array_sort = sorted(array)
    second_max = None
    first_max = None
    i = 0
    while i < len(array) - 2:
        if array[i] > array[i + 1]:
            first_max = i
            first_max_value = array[i]
        i += 1
    if first_max:
        j = first_max
    else:
        print("Yes")
        return
    while j < len(array) - 1:
        if array[j] < array[j + 1]:
            second_max = j + 1
            second_max_vale = array[j + 1]
        j +=1
    if second_max:
        if first_max > second_max:
            print("No")
            return
        else:
            if array[first_max - 1] > array[second_max - 1]:
                print("No")
                return
            else:
                print("Yes")
    else:
        if array[first_max - 1] > array[-1]:
            print("No")
            return
        else:
            print("Yes")
            return


reverse_sub_array([1, 2, 5, 4, 3])
reverse_sub_array([1, 3, 4, 10, 9, 8])
