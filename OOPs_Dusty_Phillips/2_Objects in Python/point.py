import math


class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other):
        return math.hypot((self.x - other.x), (self.y - other.y))


a = Point()
b = Point()

a.reset()
b.reset()
b.move(5, 0)
print(a.calculate_distance(b))
a.move(3, 4)
print(a.calculate_distance(b))
