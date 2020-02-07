class Vector:

    def __init__(self, dimenssion):
        self._coordinates = [0] * dimenssion

    def __len__(self):
        return len(self._coordinates)

    def __setitem__(self, key, value):
        self._coordinates[key] = value

    def __getitem__(self, item):
        return self._coordinates[item]

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coordinates == other._coordinates

    def __ne__(self, other):
        return not self._coordinates == other._coordinates

    def __str__(self):
        return "<" + str(self._coordinates)[1:-1] + ">"


v = Vector(5)
v[0] = 1
v[1] = 2
v[2] = 3
v[3] = 4
v[4] = 5

u = v + v

print(u)
