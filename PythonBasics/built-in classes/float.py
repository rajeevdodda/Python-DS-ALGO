# By default it returns 0.0
print(float())

# technically trailing "0" is optional
print(2.)

# returns float value. e2 ==> 10^2
print(2e2)

# valid string produces float value that string represent.
valid_string = '121.3'
print(float(valid_string))

# ValueError s raised
in_valid_string = "rajeev"
try:
    print(float(in_valid_string))
except ValueError as error:
    print(error)
