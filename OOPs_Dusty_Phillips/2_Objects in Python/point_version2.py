class Point:
    """ Represents a point in two-dimensional geometric coordinates """

    def __init__(self, x=0, y=0):
        self.move(x, y)

    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x, self.y = x, y

    def reset(self):
        """Reset the point back to the geometric origin: 0, 0"""
        self.move(0, 0)


point1 = Point(3, 5)
print(point1.x, point1.y)
point2 = Point()
print(point2.x, point2.y)
help(Point)
