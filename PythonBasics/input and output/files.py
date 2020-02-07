fp = open("sample.txt")

# fp.read( ) Return the (remaining) contents of a readable file as a string.
print(fp.read())

# fp.read(k) Return the next k bytes of a readable file as a string.
# once fp object is used , we cannot re use it again
print(fp.read())

new_file_object = open("sample.txt", 'r')

# prints first 20 letters
print(new_file_object.read(20))
# again prints from next letter on wards till last
print(new_file_object.read())

# fp.readline( ) Return (remainder of ) the current line of a readable file as a string.
readline_object = open("sample.txt")
print(readline_object.readline())  # appends \n at the end of the line
print(readline_object.readline())

# fp.readlines( ) Return all (remaining) lines of a readable file as a list of strings.
readlines_object = open("sample.txt")
print(readlines_object.readlines())

# Iterate all (remaining) lines of a readable file.
fp = open("sample.txt")
for line in fp:
    print("line : ", line)

# fp.seek(k) Change the current position to be at the kth byte of the file.
fp = open("sample.txt")
fp.seek(2)
# fp.tell( ) Return the current position, measured as byte-offset from the start
print(fp.tell())
print(fp.read())

# fp.write(string) Write given string at current position of the writable file.
fp = open("sample1.txt", 'w')
fp.write("Hellow world\n")
# Write each of the strings of the given sequence at the current
# position of the writable file. This command does not insert
# any newlines, beyond those that are embedded in the strings.
fp.writelines(["rajeev\n", "alhbvladfh\n"])

# Redirect output of print function to the file.
print("shfbvsjdfvksufyv", file=fp)
