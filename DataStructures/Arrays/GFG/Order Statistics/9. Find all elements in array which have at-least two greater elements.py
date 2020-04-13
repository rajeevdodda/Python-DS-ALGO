def find_elements(array: list):
    a = b = float('-inf')
    for i in array:
        if i > a:
            a, b = i, a
        elif i > b:
            b = i
    print(a)
    for i in array:
        if i < b:
            print(i, end=" ")


find_elements([2, 8, 7, 1, 5])
