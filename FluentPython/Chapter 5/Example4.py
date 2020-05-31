# Example 5-4. Sorting a list of words by their reversed spelling


def reverse_word(word):
    return word[::-1]


fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

s = sorted(fruits, key=reverse_word)

print(s)
