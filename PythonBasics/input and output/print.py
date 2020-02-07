print("rajeev", 5)

# separator between arguments, end can change print ending
print("rahul ", " king", sep="@", end="")
print(" and great")


# input function
# returns string of characters
name = input("Enter your name : ")
print(name)

year = input("In what year were you born? ")
print(type(year))

# use split() method to capture multiple information seperated with space.
reply = input("Enter x and y, separated by spaces: ")
print(reply.split())