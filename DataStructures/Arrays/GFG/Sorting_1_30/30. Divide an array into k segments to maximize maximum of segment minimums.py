def max_of_segments(a, n, k):
    if k >= 3:
        print(a)
    if k == 2:
        print(max(a[0], a[n - 1]))
    if k == 1:
        print(min(a))
    pass


max_of_segments([-10, -9, -8, 2, 7, -6, -5], 7, 2)
