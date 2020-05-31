# Example 2-20. Creating, saving, and loading a large array of floats
from array import array
from random import random


floats = array('d', (random() for i in range(10**2)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')

fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**2)
fp.close()
print(floats2[-1])
print(floats2 == floats)
