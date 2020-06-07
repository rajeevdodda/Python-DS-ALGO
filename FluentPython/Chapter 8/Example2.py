# Example 8-2. Variables are assigned to objects only after the objects are created


class Gizmo:
    def __init__(self):
        print('Gizmo id : %d', id(self))


x = Gizmo()

try:
    y = Gizmo() * 10
except TypeError as e:
    print(e)
