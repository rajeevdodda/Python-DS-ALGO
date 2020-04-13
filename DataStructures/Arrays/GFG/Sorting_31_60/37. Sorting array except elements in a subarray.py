def unsort_sub_array(array, l, u):
    new_array = array[0:l] + array[u + 1:]
    new_array.sort()
    print(new_array)
    for i in range(l):
        array[i] = new_array[i]
    for i in range(u+1, len(array)):
        array[i] = new_array[l+i -(u+1)]

    print(array)


unsort_sub_array([5, 4, 3, 12, 14, 9], 2, 4)
