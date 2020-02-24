class Node:

    def __init__(self, element):
        self._element = element
        self.next = None


class LinkedList:

    def __init__(self):
        self._head = None
        self._size = 0

    def append(self, element):
        if self._head is None:
            self._head = Node(element)
        else:
            next_element = Node(element)
            next_element.next = self._head
            self._head = next_element
        self._size += 1

    def search(self, element):
        next_element = self._head
        while next_element is not None and next_element._element != element:
            next_element = next_element.next
        return next_element

    def delete(self, element):
        next_element = self._head

        # check if head exists
        if next_element is None:
            return
        # check if element is head or not
        if next_element._element == element:
            self._head = next_element.next
            self._size -= 1
            return

        while next_element is not None and next_element._element != element:
            prev_element = next_element
            next_element = next_element.next
        if next_element is None:
            return "Element not found"
        else:
            prev_element.next = next_element.next
            self._size -= 1
            return "Element deleted"



l = LinkedList()
print(l.delete(1))
print(l._size)
print(l.append(1))
print(l._size)
print(l.search(1))
print(l.delete(1))
print(l._size)
