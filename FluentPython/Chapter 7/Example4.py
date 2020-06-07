# Example 7-4. Function reading a local and a global variable

def f1(a):
    print(a)
    print(b)


try:
    f1(3)
except NameError as e:
    print(e)

b = 6

f1(4)
