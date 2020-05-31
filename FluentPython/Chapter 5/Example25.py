# Example 5-25. Demo of methodcaller: second test shows the binding of extra arguments

from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')

print(upcase(s))

hiphenate = methodcaller('replace', ' ', '-')

print(hiphenate(s))