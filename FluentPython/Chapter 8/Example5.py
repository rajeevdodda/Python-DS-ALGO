# Example 8-5. t1 and t2 initially compare equal, but changing a mutable item inside tuple
# t1 makes it different

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)
print(t1 is t2)

print("id of t1[-1] : ", id(t1[-1]))
print("id of t2[-1] : ", id(t2[-1]))

t1[-1].append(99)
print("after modification id of t1[-1] : ", id(t1[-1]))

print(t1 == t2)


