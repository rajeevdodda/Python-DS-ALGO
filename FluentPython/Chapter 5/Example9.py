# Example 5-9. Listing attributes of functions that don’t exist in plain instances


class C:
    pass


def func():
    pass


obj = C()
print(sorted(set(dir(func)) - set(dir(obj))))

