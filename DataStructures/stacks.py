class Stack:

    def __init__(self, size):
        # initialise am empty stack.
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def stack_empty(self):
        return self.top == -1

    def push(self, x):
        self.top = self.top + 1
        if self.top == self.size:
            # reduce top by 1, bcz top will increase when push method is called.
            self.top = self.top - 1
            return "Over flow"
        self.stack[self.top] = x

    def pop(self):
        if self.stack_empty():
            return "under flow"
        else:
            self.top = self.top - 1
            return self.stack[self.top + 1]

    def peek(self):
        if self.stack_empty():
            return "stack empty"
        else:
            return self.stack[self.top]

# POP PUSH PEEK ech of the three stack operations takes O(1).


s = Stack(3)



