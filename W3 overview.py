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
print("afternoon" in var)
print("afternoon" not in var)
if "afternoon" in var:
    print("no")

#strings can be sliced to access certain parts
a = "good afternoon everyone"
print(a[5:14])

#replaces parts of strings
print(a.replace("afternoon", "evening"))
print(a.split("d"))

#concatenation combines strings
a = "hi "
b = "people"
c = a + b
print(c)

#you can use format to combine strings and other variable types
age = 16
year = 2007
intro = "I am {0} years old and I was born in {1}"
print(intro.format(age, year))

#if you want to use a character in python that already has a purpose, use escape characters

#\'  =  Single Quote	
#\\	 =  Backslash	
#\n	 =  New Line	
#\r	 =  Carriage Return	
#\t	 =  Tab	
#\b	 =  Backspace	
#\f	 =  Form Feed	
#\ooo =	Octal value	
#\xhh =	Hex value


#there are several methods that can be used on strings

"""
capitalize()   = Converts the first character to upper case
casefold()	   = Converts string into lower case
center()	   = Returns a centered string
count()	       = Returns the number of times a specified value occurs in a string
encode()	   = Returns an encoded version of the string
endswith()	   = Returns true if the string ends with the specified value
expandtabs()   = Sets the tab size of the string
find()	       = Searches the string for a specified value and returns the position of where it was found
format()	   = Formats specified values in a string
format_map()   = Formats specified values in a string
index()	       = Searches the string for a specified value and returns the position of where it was found
isalnum()	   = Returns True if all characters in the string are alphanumeric
isalpha()	   = Returns True if all characters in the string are in the alphabet
isascii()	   = Returns True if all characters in the string are ascii characters
isdecimal()	   = Returns True if all characters in the string are decimals
isdigit()	   = Returns True if all characters in the string are digits
isidentifier() = Returns True if the string is an identifier
islower()	   = Returns True if all characters in the string are lower case
isnumeric()	   = Returns True if all characters in the string are numeric
isprintable()  = Returns True if all characters in the string are printable
isspace()	   = Returns True if all characters in the string are whitespaces
istitle()	   = Returns True if the string follows the rules of a title
isupper()	   = Returns True if all characters in the string are upper case
join()	       = Joins the elements of an iterable to the end of the string
ljust()	       = Returns a left justified version of the string
lower()	       = Converts a string into lower case
lstrip()	   = Returns a left trim version of the string
maketrans()	   = Returns a translation table to be used in translations
partition()	   = Returns a tuple where the string is parted into three parts
replace()	   = Returns a string where a specified value is replaced with a specified value
rfind()	       = Searches the string for a specified value and returns the last position of where it was found
rindex()	   = Searches the string for a specified value and returns the last position of where it was found
rjust()	       = Returns a right justified version of the string
rpartition()   = Returns a tuple where the string is parted into three parts
rsplit()	   = Splits the string at the specified separator, and returns a list
rstrip()	   = Returns a right trim version of the string
split()	       = Splits the string at the specified separator, and returns a list
splitlines()   = Splits the string at line breaks and returns a list
startswith()   = Returns true if the string starts with the specified value
strip()	       = Returns a trimmed version of the string
swapcase()	   = Swaps cases, lower case becomes upper case and vice versa
title()	       = Converts the first character of each word to upper case
translate()	   = Returns a translated string
upper()	       = Converts a string into upper case
zfill()	       = Fills the string with a specified number of 0 values at the beginning
"""

#bool() will return any value as True except 0, False and emptiness

#List       = ordered  , changeable  , indexed  , Allows duplicate members
#Tuple      = ordered  , unchangeable, indexed  , Allows duplicate members
#Set        = unordered, unchangeable, unindexed, No duplicate members
#Dictionary = ordered  , changeable  , indexed  , No duplicate members

#combine lists
characters = ["a", "b", "c"]
numbers = [1, 2, 3]
characters.extend(numbers)
print(characters)