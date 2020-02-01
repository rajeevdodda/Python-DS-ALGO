class Node:

    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        # create a new node instance
        new_node = Node(data)

        # join new node next with head node
        new_node.next = self.head

        # if linked list is not empty then head is not none
        if self.head is not None:
            # join head node prev to new node
            self.head.prev = new_node

        # make new node as head node
        self.head = new_node

        # make head node(new node) prev as none
        new_node.prev = None

    def get_list(self):
        current_node = self.head
        elements = []
        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

    def search(self, x):
        current_node = self.head
        while current_node is not None and current_node.data != x:
            current_node = current_node.next
        return current_node.data if current_node else current_node

    def delete(self, x):
        current_node = self.head
        while current_node is not None and current_node.data != x:
            current_node = current_node.next

        if current_node is None:
            return None

        # change next node if deleted node is not last node
        if current_node.next is not None:
            current_node.next.prev = current_node.prev

        # change previous node if deleted node not first node
        if current_node.prev is not None:
            current_node.prev.next = current_node.next
        else:
            self.head = current_node.next


d = DoubleLinkedList()
print(d.get_list())


