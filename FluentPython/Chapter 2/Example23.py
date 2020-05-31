# Example 2-23. Working with a deque

from collections import deque
import queue
dq = deque(range(10), maxlen=10)

print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 12, 13])
print(dq)

dq.extendleft([10, 20, 30, 40])
print(dq)