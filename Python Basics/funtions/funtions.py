# "function" to describe a traditional, stateless function that is invoked
# without the context of a particular class or an instance of that class, such as sorted(data).

data = [3, 2, 1]
print(id(data))

# does not change the original list
print(sorted(data))

# "method" to describe a member function that is invoked upon a specific object using an object-oriented message
# passing syntax, such as data.sort( ).
data.sort()
# modifies original list
print(data, id(data))
