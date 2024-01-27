#store multipleitems in 1 variable
#can't change
#indexed
#store any data types

#examples of tuples
tuples = ("one", "two", "three", "four")
tuples = ("one", "one", "two", "three", "three", "three")
tuples = ("one",)


#accessing tuples
tuples = ("one", "two", "two", "three", "four", "four")
print(tuple[1])   #first item
print(tuple[-1])  #last item
print(tuple[1:4]) #range
print(tuple[:3])  #from start until number
print(tuple[2:])  #from number until end
if "three" in tuples:
    print("three is in this tuple")

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


