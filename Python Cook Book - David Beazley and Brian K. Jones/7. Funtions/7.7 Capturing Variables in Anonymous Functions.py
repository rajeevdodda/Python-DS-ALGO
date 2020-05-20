x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

# the value of x used in the lambda expression is a free variable that gets bound at runtime, not definition time.
print(a(10), b(10))

# include the value as a default value, If you want an anonymous function to capture a value at the point of definition
x = 10
c = lambda y, x=x: x + y

x = 20
d = lambda y, x=x: x + y

print(c(10), d(10))

funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))

funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print(f(0))
