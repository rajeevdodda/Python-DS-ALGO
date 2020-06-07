# Example 8-8. Bus picks up and drops off passengers
import copy


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus = bus1
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(id(bus1), id(bus), id(bus2), id(bus3))

bus1.drop('Bill')

print(bus2.passengers)

print(id(bus1.passengers), id(bus.passengers), id(bus2.passengers), id(bus3.passengers))

print(bus3.passengers)