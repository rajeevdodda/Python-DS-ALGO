from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
    pass


if __name__ == "__main__":
    with open('somefile.txt') as f:
        print(type(f))
        for line, prev_line in search(f, 'python', 3):
            for pline in prev_line:
                print(pline, end="")
            print(line, end="")
            print('-' * 20)
            pass

# Using creates a fixed-sized queue. When new items are added and deque(maxlen=N) the queue is full,
# the oldest item is automatically removed.
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
print(d)
d.append(4)
print(d)


# Adding or popping items from either end of a queue has O(1) complexity. This is unlike
# a list where inserting or removing items from the front of the list is O(N).
d.appendleft(0)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
