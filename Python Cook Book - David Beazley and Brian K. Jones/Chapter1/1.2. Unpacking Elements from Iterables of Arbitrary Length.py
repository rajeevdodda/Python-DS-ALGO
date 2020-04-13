record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

# phone_numbers will be converted into list
print(phone_numbers)

record2 = ('Dave', 'dave@example.com')
name1, email1, *phone_numbers = record2
# *phone_numbers returns empty list i.e., None
print(phone_numbers)

# The starred variable can also be the first one in the list.
*s, t = "hello"
print(s, t)

# s becomes empty list
*s, t, u = "uh"
print(s, t, u)

# clever recursive algorithm for sum of elements
items = [1, 2, 3, 4, 5]


def items_sum(items):
    head, *tail = items
    return head + items_sum(tail) if tail else head


print(items_sum(items))
