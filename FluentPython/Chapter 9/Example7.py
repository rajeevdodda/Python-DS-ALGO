# Example 9-7. vector2d_v3.py: only the changes needed to make Vector2d immutable
# are shown here; see full listing in Example 9-9
from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


v1 = Vector2d(3, 4)
print(v1)

print(v1.x)
v1._Vector2d__x = 11

try:
    v1.x = 10
except AttributeError as e:
    print(e)

v2 = Vector2d(3.1, 4)

print(hash(v1), hash(v2))
print(v1 == v2)

print(v1.__dict__)
print(v1._Vector2d__x)