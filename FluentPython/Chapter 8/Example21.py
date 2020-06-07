# Example 8-21. String literals may create shared objects

t1 = tuple(range(100000))
t2 = tuple(range(100000))

print(id(t1), id(t2))
print(t1 == t2)
print(t1 is t2)


s1 = "ABC"
s2 = "ABC"

print(id(s1), id(s2))
print(s1 == s2)
print(s1 is s2)

a = (5, 5,5,5,5,5,5,5,5,5,5,5)
b = (5, )
print(id((a)), id((b)))