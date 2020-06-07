# Example 8-3. charles and lewis refer to the same object

charles = {'name': 'Charles L. Dodgson', 'born': 1832}

lewis = charles
print(lewis is charles)

print("charles id : ", id(charles), " ", "lewis id : ", id(lewis) )