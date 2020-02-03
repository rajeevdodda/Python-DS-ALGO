# Python’s built-in sequence types (str, tuple, and list) support the following operator syntax's:
s = "rajeev"
l = [1, 2, 3, 4]
t = (1, 2, 3, 4)

# element at index j
print(s[1], l[2], t[0])

# [start:stop]
print(s[1:3], l[1:3], t[1:4])

# [start:stop:step]
print(s[0:5:2], l[0:3:2], t[0:5:1])

# concatenation of sequences
print(s + " rahul")
print(l + [1])
print(t + (1,))

# k * s ==> short hand notation of s + s + s ..... k times
print(s * 3)
print(l * 2)
print(t * 2)

# "in" operator to check value in container.. similarly "not in"
print('r' in s)
print(10 in l)
print(2 in t)

# reverse a sequence
print(t[::-1])

del l[0]
# del satement removes elements from mutable objects
print(l)

try:
    del t[0]
except TypeError as error:
    print(error)

# "in" can be used to check whether a value is present in sequence
print("ee" in s)
print(1 in t, 10 in l)

# All sequences define comparison operations based on lexicographic order
print("rahul" > "Rahul", "ab" > 'aa')  # returns false and true
print([5, 6, 7] < [5, 9])  # returns true

print([5] == [5])  # returns true

# Operators in Sets, Frozenset, Dictionary

# Set and Frozenset operations ==> in, not in, >, >=, <, <=, ==, !=, |,  &, - ,^
set_a = {1, 2, 3}
set_b = {4, 5, 3}
set_aa = {1, 2}

print(1 in set_a, 10 not in set_b)  # return true

print(set_a is set_b, set_a == set_b)  # returns false and true

print(set_aa < set_a)  # returns true ( < proper subset)

print(set_b | set_a)  # union of b and a
print(set_a & set_b)

print(set_a - set_b)  # elements in a but not in b
print(set_a ^ set_b)  # elements in a and b but not in both

dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_bb = {'e': 5}
dict_b = {'a': 2, 'b': 2, 'c': 3}

print(dict_b == dict_a)  # should contain same key value pairs
dict_a['a'] = 2  # change value of a key
print(dict_a)

print('a' in dict_a, 'z' not in dict_a)  # in is used to check key



