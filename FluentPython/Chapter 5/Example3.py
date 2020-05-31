# Example 5-3. Sorting a list of words by length

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

s = sorted(fruits, key=len)

print(s)