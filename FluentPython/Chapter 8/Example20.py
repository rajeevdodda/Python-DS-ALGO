# Example 8-20. A tuple built from another is actually the same exact tuple

t1 = (1, 2, 3)
t2 = tuple(t1)
t3 = t1[:]

print(t1 is t2, t1 is t3)