# Example 8-10. Cyclic references: b refers to a, and then is appended to a; deepcopy still
# manages to copy a

from copy import deepcopy


a = [10, 20]
b = [a, 30]

a.append(b)

print(a)

c = deepcopy(a)
print(c)