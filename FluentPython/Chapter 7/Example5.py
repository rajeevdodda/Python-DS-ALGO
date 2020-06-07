# Example 7-5. Variable b is local, because it is assigned a value in the body of the function

b = 6


def f2(a):
    print("in f2")
    print(a)
    print(b)
    b = 9


try:
    f2(3)
except NameError as e:
    print(e)


def f3(a):
    print("in f3")
    global b
    print(a)
    print(b)
    b = 9


f3(2)

print(b)
