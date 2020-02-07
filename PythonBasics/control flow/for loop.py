# for loop can be used on any iterable structure  like, str, list, tuple, set, dict, file
l = [1, 2, 3]
t = (1, 2, 3)
s = {1, 2, 3}
dict_a = {'a': 1, 'b': 2, 'c': 3}

for i in l:
    print("list : ", i)

for i in t:
    print("tuple : ", i)

for i in s:
    print("set : ", i)

# prints keys
for i in dict_a:
    print("dict : ", i)
