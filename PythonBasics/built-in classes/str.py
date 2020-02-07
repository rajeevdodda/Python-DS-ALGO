# Strings can be enclosed in '' or " "

# back slash as escape character
new_string = 'Dont\'t worry'
print(new_string)

# the backslash must itself be escaped to occur as a natural character of the string literal
print('C:\\Py\nthon\\')

# The advantage of such triple-quoted strings is that newline characters can be embedded naturally
# (rather than escaped as \n).
print("""Hello world.
My name is rajeev""")

# returns list as string
print(str([1, 2, 3]))