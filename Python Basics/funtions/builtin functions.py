# returns absolute value of a number
print(abs(-1))

# Return True if bool(e) is True for each element e.
print(all([True, '1', 1]))  # true
print(all([[], 1, True]))  # false

# Return True if bool(e) is True for at least one element e.
print(any([True, '1', 1]))  # true
print(any([[], "", False]))  # false

# chr(integer) Return a one-character string with the given Unicode code point.
print(chr(66))

# divmod(x, y) Return (x // y, x % y) as tuple, if x and y are integers.
print(divmod(11, 5))

# hash(obj) Return an integer hash value for the object.
try:
    print(hash([1, 4]))
except TypeError as error:
    print(error)

print(hash((1, 4)))

# id(obj) Return the unique integer serving as an “identity” for the object.
l = [1, 2]
print(id(l))

# input(prompt) Return a string from standard input; the prompt is optional.

# isinstance(obj, cls) Determine if obj is an instance of the class (or a subclass).
print(isinstance([1, 2], list))

# iter(iterable) Return a new iterator object for the parameter.
print(iter('rajeev'))

# len(iterable) Return the number of elements in the given iteration.
print(len("rajeev"), len({1, 2, 4}))


def square(a):
    return a * a


# map(f, iter1, iter2, ...) Return an iterator yielding the result of function calls f(e1, e2, ...)
# for respective elements e1 ∈ iter1,e2 ∈ iter2, ...
print(list(map(square, [1, 2, 3])))

# max(iterable) Return the largest element of the given iteration.
# max(a, b, c, ...) Return the largest of the arguments.
# similarly for min()

print(max([1, 2, 4]), max({1: 5, 2: 6, 10: 1}))
print(max(1, 5, 6, 7))

# next(iterator) Return the next element reported by the iterator
iter_object = iter("rahul")
try:
    print(next(iter_object))
    print(next(iter_object))
    print(next(iter_object))
    print(next(iter_object))
    print(next(iter_object))
    print(next(iter_object))
    print(next(iter_object))
    print(next(iter_object))
except StopIteration as error:
    print(error)

# open(filename, mode) Open a file with the given name and access mode
print(open("sample.txt"), 'r')

# ord(char) Return the Unicode code point of the given character.
print(ord('A'))

# pow(x, y) Return the value xy (as an integer if x and y are integers); equivalent to x y.
print(pow(10, 10))

# pow(x, y, z) Return the value (xy mod z) as an integer.
print(pow(6, 2, 5))

# range(start, stop, step) Construct an iteration of values start, start+step, start+2 step,
print(list(range(10)), list(range(5, 10)), list(range(0, 10, 2)))

# reversed(sequence) Return an iteration of the sequence in reverse.
print(list(reversed([1, 2, 4])), (reversed("rahul")))

# round(x) Return the nearest int value (a tie is broken toward the even value).
# round(x, k) Return the value rounded to the nearest 10−k (return-type matches x).
print(round(1.6), round(-1.6), round(1.5), round(1.3), round(-1.3))

# sorted(iterable) Return a list containing elements of the iterable in sorted order.
print(sorted([1, 2, 0]), sorted("rahul"), sorted({1, 2, 0}))

# sum(iterable) Return the sum of the elements in the iterable (must be numeric).
print(sum([1, 2, 4]))

# type(obj) Return the class to which the instance obj belongs.
print(type({1, 3}))
