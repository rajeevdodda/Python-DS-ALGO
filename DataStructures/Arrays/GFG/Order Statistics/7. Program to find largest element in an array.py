def max_array(array:list):
    a = float('-inf')
    for i in array:
        if i > a:
            a = i
    print(a)


max_array([20, 10, 20, 4, 100])