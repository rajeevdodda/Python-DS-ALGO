# default arguments appear last
def spam(a, b=42, *args, c=3):
    print(args)
    print(a + b + c)


# after *args keyword args must me assigned to get the changed value
spam(1, 2, 3, 4, 5)  # c = 3

spam(1, 2, c=8)  # c = 8, args = ()


# If the default value is supposed to be a mutable container, such as a list, set, or dictionary,
# use None as the default
def spam2(a, b=None):
    if b is None:
        b = []
    print(sum(b))


spam2(1)
spam2(2, [1, 2, 4])

_no_value = object()

print(_no_value)


# If, instead of providing a default value, you want to write code that merely tests whether
# an optional argument was given an interesting value or not, use this idiom:
def spam3(a, b=_no_value):
    print(type(b))


spam3(1, 2)
spam3(1, None)

#######################################################################################################################

x = 42


def spam4(a, b=x):
    return b


print(spam4(1))  # print 42

x = 1
# changing the variable x (which was used as a default value) has no effect.
# the values assigned as defaults should always be immutable objects, such as None, True, False, numbers, or strings.
print(spam4(2))  # prints 42


def spam5(a, b=[]):
    return b


# if the default value ever escapes the function and gets modified. Such changes will permanently alter the
# default value across future function calls
d = spam5(1)
d.append(1)
print(d)

e = spam5(2)
print(e)


# To avoid this, it’s better to assign None as a default and add a check inside the function

def spam6(a, b=None):
    # if not b: # NO! Use 'b is None' instead.
    # The problem here is that although None evaluates to False, many other objects (e.g.,
    # zero-length strings, lists, tuples, dicts, etc.) will create silent error
    if b is None:
        b = []
    return b


g = [1, 2, 4]
z = spam6(1, g)
print(z)
g.append(1)
print(z)

r = spam6(1)
r.append(1)

s = spam6(2)
s.append(4)
print(r, s)
print(spam6(1, 0))


def spam7(a, b=None):
    if not b:
        b = []
    return b


x = []
print(spam7(1, b=x))
x.append(3)
print(spam7(1))
print(spam7(1, 0))
