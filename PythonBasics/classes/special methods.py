class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __add__(self, other):
        return self._name + " " + other._name

    def __sub__(self, other):
        return self._age - other._age

    def __getitem__(self, item):
        try:
            return self._name[item]
        except IndexError as error:
            return error

    def __len__(self):
        return len(self._name)

    def __bool__(self):
        return False

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self._name):
            result = self._name[self.index]
            self.index += 1
            return result
        else:
            raise IndexError

    def __eq__(self, other):
        return self._name == other._name


person_1 = Person("rajeev", 23)
person_2 = Person("rahul", 25)

try:
    print(person_1 + person_2)
except TypeError as error:
    print(error)

print(person_1 - person_2)

print((person_2[10]))

print(len(person_2))

print(bool(person_2))

print(iter(person_2))
print(next(person_2))
print(next(person_2))
print(next(person_2))
print(next(person_2))
print(next(person_2))

print(type(None))  # returns None type class

print(person_2 is person_1)

print(person_1 == person_2)  # uses "is" functionality if __equal__ is not implemented

