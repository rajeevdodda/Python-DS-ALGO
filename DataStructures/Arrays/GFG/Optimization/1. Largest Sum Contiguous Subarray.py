def max_sub_array(array: list):
    best_sum = current_sum = array[0]
    best_start = best_end = 0

    i = 1
    while i < len(array):
        if current_sum <= 0:
            current_sum = array[i]
            current_start = i
        else:
            current_sum += array[i]

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = i

        i += 1


    print(best_start, best_end, best_sum)


max_sub_array([-2, -3, 4, -1, -2, 1, 5, -3])
