# By default it returns "False"
bool_return_value = bool()
print(bool_return_value)

# returns "True"
bool_return_value = bool(True)
print(bool_return_value)

# Numbers evaluate to "False" if zero, and "True" if nonzero.
zero = 0
print(bool(zero))

non_zero = 5
print(bool(non_zero))


# Sequences and other container types, such as strings and lists, evaluate to "False" if empty and "True" if nonempty.
empty_list = list()
empty_tuple = tuple()
empty_set = set()
empty_dict = dict()

print(bool(empty_list), bool(empty_tuple), bool(empty_set), bool(empty_dict))
