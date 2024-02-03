#square brackets show it is a list
#each item in the list is in quotation marks and is seperated from the rest by a comma

#to print the entire contents of a list with the square brackets, commas and quotation marks
bicycles = ["trek", "cannondale", "redline", "specialised"]
print(bicycles)

#print a specific item in the list
#index positions start at 0 not 1
ice_cream = ["strawberry", "vanilla", "chocolate", "mint"]
print(ice_cream[0])
print(ice_cream[1].upper())

#-1 means the last item in a list, -2 the second last, ect, ect
print(ice_cream[-1].title())

#items in a list can be used like a variable
#making an f-string using a value from a list
ice_cream = ["strawberry", "vanilla", "chocolate", "mint"]
message = f"my favourite ice-cream flavour is {ice_cream[3]}!"
print(message.title())

#modifying items in a list
chocolates = ["white", "milk", "dark", "chilli"]
print(chocolates)
chocolates[3] = "caramel"
print(chocolates)

#adding new items to the end of a list
chocolates = ["white", "milk", "dark"]
chocolates.append("orange")
print(chocolates)
#this can be used to add data one at a time to a blank list
chocolates = []
chocolates.append("white")
chocolates.append("milk")
chocolates.append("dark")
chocolates.append("mint")
print(chocolates)

#adding items into a list in a specific place
chocolates = ["white", "dark", "toffee"]
chocolates.insert(1, "milk")
print(chocolates)

#removing an item from a list
chocolates = ["white", "fudge", "milk", "dark"]
del chocolates[1]
print(chocolates)

#deleting the last item from a list so you can still access it
chocolates = ["white", "milk", "dark", "amaretto"]
popped_chocolates = chocolates.pop()
print(chocolates)
print(popped_chocolates)

#deleting items from a specific position in a list
chocolates = ["white", "milk", "cherry", "dark"]
popped_chocolates = chocolates.pop(3)
print(chocolates)
print(popped_chocolates)

#deleting items by name not value
chocolates = ["white", "milk", "crispy", "dark"]
chocolates.remove("crispy")

#deleting an item by value so you can still access it
chocolates = ["white", "milk", "extra dark", "dark"]
not_selling = "extra dark"
chocolates.remove(not_selling)
print(chocolates)
print(f"\n{not_selling.title()} wasnt selling well enough")

#permanently making a list alphabetical/reverse-alphabetical
animals = ["dog", "cat", "rabbit", "hamster", "snake"]
animals.sort()
print(animals)
animals = ["dog", "cat", "rabbit", "hamster", "snake"]
animals.sort(reverse=True)
print(animals)

#temporarily make list alphabetical/reverse-alphabetical

#reverse a list
animals = ["dog", "cat", "rabbit", "hamster", "snake"]
animals.reverse()
print(animals)

#find how many items in a list
animals = ["dog", "cat", "rabbit", "hamster", "snake"]
print(len(animals))

