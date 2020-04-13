def make_median(array, x, n):
    less_than = 0
    greater_than = 0
    equal = 0
    for i in array:
        if i == x:
            equal += 1
        elif i > x:
            greater_than += 1
        elif i < x:
            less_than += 1
    if less_than < (n + 1) // 2 <= less_than + equal:
        print(0)
        return
    else:
        print(abs((less_than + 1) * 2 - n - 1))


if __name__ == '__main__':
    array_list = [2, 2, 3]
    make_median(array_list, 2, len(array_list))
