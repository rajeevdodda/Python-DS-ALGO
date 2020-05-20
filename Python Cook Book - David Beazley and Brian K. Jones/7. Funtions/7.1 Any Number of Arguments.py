def avg(first, *rest):
    # *rest is a tuple of all the extra positional arguments passed.
    print(type(rest))
    print(rest)
    print((first + sum(rest)) / (1 + len(rest)))


avg(1, 3, 2)
avg(1, *[3, 2])


# arguments are tuples and dictionaries.
def anyargs(*args, **kwargs):
    print(type(args), type(kwargs))


anyargs()


# only keyword arguments can appear after *args.
def a(x, *args, z, **kwargs):
    print(x, args, z, kwargs)


a(1, 1, z=2, t=100)
