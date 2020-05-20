def add_function(x: int, y: int) -> int:
    return x + y


print(help(add_function))
# Function annotations are merely stored in a function’s __annotations__ attribute
print(add_function.__annotations__)
