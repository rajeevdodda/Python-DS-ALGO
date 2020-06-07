# Example 8-4. alex and charles compare equal, but alex is not charles

charles = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

lewis = charles
print(lewis is charles)
print(alex is not  charles)

print("charles id : ", id(charles), " ", "lewis id : ", id(lewis),  " ", "alex id : ", id(alex))

