def max_three(array: list):
    a = b = c = float('-inf')
    for i in array:
        if i > a:
            a, b, c = i, a, b
        elif i > b:
            b, c = i, b
        elif i > c:
            c = i
    print(a, b, c)


    pass


max_three([10, 4, 3, 50, 23, 90])
