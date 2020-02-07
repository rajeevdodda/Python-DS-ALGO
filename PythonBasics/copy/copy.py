import copy


a = [1]
b = [2]
c = [3]
list_a = [a, b, c]
list_e = [a, b, c]
print(id(list_a))

list_b = list_a

print(id(list_a) == id(list_b))  # returns true

# shallow copy
list_c = list(list_a)  # this creates a new list but refers to same elements
list_a[0].append(1)  # changes list_c also

print(list_c, list_a)
print(id(list_c) == id(list_b))  # returns false

# deep copy
list_d = copy.deepcopy(list_e)
list_a[0].append(3)
print(list_a, list_c, list_d)
