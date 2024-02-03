#casting is assigning a type to a variable
#variables are automatically given a type but this lets you choose its type
x = str("6")

#this prints the type of the variable
print(type(x))

#you can assign multiple variable's values in one line
a, b, c = "one", "two", "three"
A = B = C = "hi"
colours = "red", "yellow", "green"
r, y, g = colours

#global variables are created outside functions and can be used throughout your code
#local variables are created in functions and can only be used in that function
#if you define a varibale in a function as global, it becomes global
x = "hello"
def function():
    y = "world"
    global z
    z = "bye"
    print(x, y, z)
function()

#there are many different types of variable
"""Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""

#triple quotes make strings that can have multiple lines

#characters in strings can be accessed just like characters in lists
var = "good morning"
print(var[0])
for i in var:
    print(i)

#in checks if a string is in a string and prints the result as a bool
print ("free" in var)
