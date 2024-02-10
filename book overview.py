#f-strings
integer_one = "hello"
integer_two = "world"
f_string = f"{integer_one} {integer_two} :)"
print(f_string)

#changing cases
print("hello".upper())
print("hello".lower())
print("hello".title())

#adding tabs
print("\thello")
#adding lines
print("\nhello")

#removing whitespace permanently
integer_one = " hello "
integer_one = integer_one.rstrip()
integer_one = integer_one.lstrip()
integer_one = integer_one.strip()

#removing prefixes and suffixes
integer_one = "pre.main.suff"
integer_one = integer_one.removeprefix("pre.")
integer_one = integer_one.removesuffix(".suff")
print(integer_one)

#lists
list = ["int_1", "int_2", "int_3", "int_5"]
print(list)
print(list[0])
print("this is an f-string", list[0])

#editing lists
list = ["int_1", "int_2", "int_3", "int_5"]
list[3] = "int_4"        #change item
list.append("int_5")     #add item to end of list
list.insert(0, "int_0")  #add item to list in specific place
del list[4]              #permanent removal using placement of item in list
popped_list = list.pop() #last item removed and is stored seperately in new variable
popped_list = list.pop(3)#specific item removed and is stored seperately in new variable
list.remove("int_0")     #permanent removal using name of item in list
integer_1 = "int_1"      #specific item is removed and stored seperately in new variable }
list.remove(integer_1)   

#ordering lists
list = ["b1", "c1", "e1", "a1", "d1"]
list.sort()                 #permanently order the list alphabetically
list.sort(reverse=True)     #permanently order the list reverse-alphabetically
list.reverse()              #permanently reverse order of list
sorted = sorted(list)       #1st way to temporarily sort a list alphabetically
 #couldnt figure out how to temporarily sort 2nd way (bottom of page43 in book)
print(len(list))                  #find how many items in a list

#for loops
integers = ["integer_1", "integer_2", "integer_3"]
for integer in integers:                                 #prints each value in th list
    print(integer)       
for integer in integers:                                 #adding text into and after for loops
    print(f"{integer}, is a value in the list")
for value in range(1, 5):                                #print all values within range excluding final number
    print(value)

