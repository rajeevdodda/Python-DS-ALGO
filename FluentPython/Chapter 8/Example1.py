# Example 8-1. Variables a and b hold references to the same list, not copies of the list

a = [1, 2, 3]
b = a
a.append(4)

print(a, b)