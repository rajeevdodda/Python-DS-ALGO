r = range(0, 101, 2)
print(type(r))  # returns range class
print(r[10])  # supports indexing
print(len(r))  # returns length


class Range:

    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("step size cant be 0")
        if stop is None:
            start, stop = 0, start

        self._length = (stop - start + step - 1) // step
        self._start = start
        self._stop = stop
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        if item < 0:
            item += self._length

        if not 0 <= item < self._length:
            raise IndexError('Index out of range error')

        return self._start + item * self._step


R = Range(100)
print(R[99])

