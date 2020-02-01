class Queues:

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.queue = [None] * capacity
        self.size = 0

    def enqueue(self, x):
        if self.overflow():
            print("over flow")
            return "over flow"
        self.queue[self.tail] = x
        self.size = self.size + 1
        self.tail = self.tail + 1

        if self.tail == self.capacity:
            self.tail = 0

    def dequeue(self):
        if self.underflow():
            print("under flow")
            return "under flow"
        x = self.queue[self.head]
        self.head = self.head + 1
        self.size = self.size - 1
        if self.head == self.capacity:
            self.head = 0
            pass
        return x

    def overflow(self):
        return self.size == self.capacity

    def underflow(self):
        return self.size == 0


q = Queues(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.tail, q.head)
print(q.queue)

print(q.dequeue())
q.enqueue(5)
print(q.queue)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.dequeue()


