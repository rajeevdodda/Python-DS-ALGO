# Example 1-2. A simple two-dimensional vector class

from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __str__(self):
        return str("Vector")

    def __bool__(self):
        return bool(abs(self))

    # faster implementation
    # def __bool__(self):
    #     return bool(self.x or self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 3)
v2 = Vector(1, 2)
print(v1)
v3 = v1 + v2
print(v3 * 2)
print(abs(v3))
v4 = Vector()
print(bool(v4))
