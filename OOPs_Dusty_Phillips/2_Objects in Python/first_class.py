class Point:
    """ They must start with a letter or underscore, and can only be comprised of
letters, underscores, or numbers. They should be named using CamelCase notation"""

    def reset(self):
        self.x = 0

    def spam():
        pass


a = Point()
b = Point()
print(a, b)

try:
    print(a.x)
except AttributeError as error:
    print(error)

# We cam set arbitrary attributes on an instantiated object using the dot notation.
a.x, a.y = 10, 20
print(a.x, a.y)

a.reset()
print(a.x, a.y)

a.x = 10
print(a.x)
# we can invoke the function on the class, explicitly passing our object as the self argument
Point.reset(a)
print(a.x)

try:
    a.spam()
except TypeError as error:
    print(error)
