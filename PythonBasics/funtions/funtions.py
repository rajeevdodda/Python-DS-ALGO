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


# data , target are formal parameters
def count(data, target):
    n = 0
    for i in data:
        if i == target:
            n += 1
    # without an argument "None" value is returned
    return n


# data, 1 are actual parameters that are used by the caller to call function.
# the objects sent to function are not copied, bt reference is sent.
print(count(data, 1))

# Mutable parameters : list, set, dict
sample_list = [1, 2, 3]
sample_set = {1, 2, 3}
sample_dict = {"a": 1, "b": 2}


def operations_on_mutable_objects(l, s, d):
    l.append(10)
    s.add(11)
    d["c"] = 3
    return l, s, d


print("operation", operations_on_mutable_objects(sample_list, sample_set, sample_dict))
# the above function will change mutable objects state
print("after operation ", sample_list, sample_set, sample_dict)


def reassign_mutable_objects(l, s, d):
    l = list()
    s = set()
    d = dict()
    return l, s, d


print("re-assign", reassign_mutable_objects(sample_list, sample_set, sample_dict))
# the above function will not change mutable objects state as the function is re assigning.
print("after re-assign ", sample_list, sample_set, sample_dict)


# default parameter values
# if a default parameter value is present for one parameter, it must be present for all further parameters.
def parameter(a, b=12, c=11):
    return a, b, c


# returns -5 bcz of key=abs, it compares abs(-5) with abs(1)
print(max(-5, 2, key=abs))

