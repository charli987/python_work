#for loops

#printing out each item in a list using a for loop
girls = ["bella", "alice", "carly", "darcie", "evie"]
for girl in girls:
    print(girl)
    #line 5 tells the computer that it needs to get the first value in the list and associate it with the variable 'girl'
    #line 6 tells the computer to print this
    #because there are more values, the computer goes back to the first line of the for loop and repeats the instructions until there arent any variables left
    #the temporary variable 'girl' can be anything but it makes the code easier to read if it is connected to the list name

#printing using for loops
girls = ["bella", "alice", "carly", "darcie", "evie"]
for girl in girls:
    print(f"{girl}, you are very pretty!") 
    print(f"i love your hair, {girl}")
    #anything indented under the for loop is repeated for every value
    #you can put as much as you want in a for loop
    
#printing after for loops
girls = ["bella", "alice", "carly", "darcie", "evie"]
for girl in girls:
    print(f"{girl}, you are very pretty!") 
    print(f"i love your hair, {girl}")
print("it was nice to meet you all")
    #anything on the same indentation as the for loop will be executed after the for loop is completed
    

#using the range() function

#generating a series of numbers
for value in range(1, 5):
    print(value)
    #this will only print 1 2 3 4 because python stops counting when it reaches the 2nd number so doesn't print it
for value in range(5):
    print(value)
    #this does the same as the previous code but starts from 0 so prints 0 1 2 3 4 
    
#creating a variable that is a list of numbers
numbers = list(range(1, 5))
print(numbers)

#skipping numbers in a given range
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)
   #if you put a 3rd value in a range loop, the computer adds that value each time until it gets bigger than the second number
   
#listing square numbers
#method 1
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
    #the computer takes the firt number in the range(1) and squares it then adds it to the end of the empty list squares
    # it repeats this for every value in the range (1-11)
#method 2
squares = []
for value in range(1, 11):
    squares.append(value ** 2)   
print(squares)
    #more consise
#method 3
squares = [value ** 2 for value in range(1, 11)]
print(squares)
    # more consise

    