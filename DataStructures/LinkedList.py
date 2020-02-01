class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def search(self, k):
        """ search takes O(n) times in worst case """
        current_node = self.head
        while current_node is not None and current_node.data != k:
            current_node = current_node.next

        if current_node:
            return current_node.data
        else:
            return current_node

    def insert(self, new_node):
        new_node.next = self.head
        self.head = new_node
        return True

    def insert_last(self, new_node):
        """ insertion takes O(1) time. """
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    def get_list(self):
        current_node = self.head
        elements = []
        if current_node is None:
            return elements
        while True:
            elements.append(current_node.data)
            if current_node.next is None:
                break

            current_node = current_node.next
        return elements

    def delete(self, x):
        if self.head is None:
            return None

        if self.head.data == x:
            self.head = self.head.next
            return True

        current_node = self.head
        while current_node is not None and current_node.data != x:
            pre_node = current_node
            current_node = current_node.next
        if current_node:
            pre_node.next = current_node.next
            return True
        else:
            return False


linked_list_instance = LinkedList()

linked_list_instance.insert(Node(1))
linked_list_instance.insert(Node(2))
linked_list_instance.insert(Node(3))
linked_list_instance.insert_last(Node(4))
print(linked_list_instance.get_list())