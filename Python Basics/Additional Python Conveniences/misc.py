# conditional expressions

# expr1 if condition else expr2
print("a" if 3 > 4 else "b")

# comprehension syntax

data_list = list(range(100))

# [ expression for value in iterable if condition ]
print([d for d in data_list if d % 5 == 0])

print([d * d for d in data_list if d % 5 == 0])

# list comprehension
print("Squares : ", [k * k for k in range(10)])

# set comprehension
print("Squares : ", {k * k for k in range(10)})

# dict comprehension
print("Squares : ", {k: k * k for k in range(10)})

# there is no tuple comprehension

# generator comprehension
print("Squares : ", (k * k for k in range(10)))  # returns generator object
print("sum of squares using generator : ", sum((k * k for k in range(10))))

# packing and unpacking

# treated as tuple "automatic packing"
t = 1, 2, 4
print(t)


def abc():
    return 1, 3


# returns tuple
print(abc())

# unpacking, right hand side should be sequence type of same length
a, b, c = [1, 2, 3]
print(a, b, c)

a, b, c = (1, 2, 3)
print(a, b, c)

a, b, c = {1, 2, 3}
print(a, b, c)

a, b, c, d = range(7, 11)
print(a, b, c, d)

a, b = "ab"
print(a, b)

# assigns key values
a, b = {"c": 1, "d": 2}
print(a, b)
