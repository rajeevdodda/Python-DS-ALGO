def alternative_sorting(array: list):
    array.sort()
    n = len(array)
    i, j = 0, n - 1
    while i < j:
        print(j, i, end=" ")
        i, j = i + 1, j - 1
    if n % 2 != 0:
        print(array[j])


if __name__ == '__main__':
    alternative_sorting(list(range(9)))

# Time Complexity: O(n Log n)
# Auxiliary Space : O(1)
