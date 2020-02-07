# By default int constructor return "0".
print(int())

# We can express integer value in binary, octal, hexadecimal format.
print(0b1011, 0o52, 0x7f)

# converts floating point to int.
print(int(1.34))

# valid string produces integral value that string represent, base 10.
valid_string = '121'
print(int(valid_string))

# ValueError s raised
in_valid_string = "rajeev"
try:
    print(int(in_valid_string))
except ValueError as error:
    print(error)
