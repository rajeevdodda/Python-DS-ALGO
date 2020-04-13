def product(array: list, k):
    array.sort()
    ans = 1
    for i in array[:k]:
        ans *= i
    print(ans)


product([198, 76, 544, 123, 154, 675], 2)