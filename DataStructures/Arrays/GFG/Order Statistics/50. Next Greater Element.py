from DataStructures.Stacks.stacks_normal import *


def next_greater_element(array):
    s = Stack()
    for i in array:
        if not s.is_empty():
            while s.top_element() < i:
                print(s.pop(), " -- ", i)
                if s.is_empty():
                    break

        s.push(i)

    while not s.is_empty():
        print(s.pop(), " -- ", "-1")


if __name__ == '__main__':
    array_list = [11, 13, 21, 3]
    next_greater_element(array_list)
    next_greater_element(list(range(10)))
    next_greater_element(list(range(10, 1, -1)))
