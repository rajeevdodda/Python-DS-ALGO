# Example 3-13. Build a set of Latin-1 characters that have the word “SIGN” in their Unicode names

from unicodedata import name

for i in range(32, 256):
    print(i, name(chr(i), "no name"))

s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(s)


hash()