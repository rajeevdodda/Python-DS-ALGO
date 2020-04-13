def check_interval(array):
    array.sort(key=lambda x: x[0])
    i = 0
    while i < len(array) - 1:
        if array[i][0] == array[i + 1][0]:
            if array[i][1] != array[i + 1][i]:
                print("True")
                return
        i += 1
    print("False")


check_interval([[1, 3], [3, 7], [4, 8], [2, 5]])
