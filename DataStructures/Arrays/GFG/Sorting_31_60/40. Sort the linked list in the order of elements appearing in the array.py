class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.tail = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next


def sort_linked_list(array, head):
    temp = head
    sample_dict = dict()
    while temp is not None:
        sample_dict[temp.data] = sample_dict.get(temp.data, 0) + 1
        temp = temp.next
    print(sample_dict)
    temp = head
    for j in array:
        frequency = sample_dict.get(j, 0)
        while frequency > 0:
            temp.data = j
            temp = temp.next
            frequency -= 1





l = LinkedList()

array = [5, 1, 3, 2, 8]
linked_list_data = [3, 2, 5, 8, 5, 2, 1]
for i in linked_list_data:
    l.push(i)
print()
l.print_list()
print()
print(l.head.data)
sort_linked_list(array, l.head)
l.print_list()
