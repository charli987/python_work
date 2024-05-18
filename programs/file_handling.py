# "r" = read = opens file for reading
# "a" = append = opens file for appending or creates one if this doesnt exist
# "w" = write = opens file for writng or creates one if this doesnt exist
# "x" = create = creates a file

# "t" = text = file should be handled in text mode
# "b" = binary = file should be handled in binary mode

# r and t are default values so don't need to be specified

f = open("C:\Users\charl\OneDrive\Documents\CV plan.docx")   
print(f.read())              #opens file that's in a different location

f = open("demofile.txt")     #opens file for reading
print(f.read())              #prints content of file
print(f.read(5))             #prints specified number of characters
print(f.readline())          #prints first line of file
print(f.readline())          #prints second line of file
f.close()                    #closes file

f = open("demofile.txt", "a")             #opens and lets you append file
f.write("the file now has more content")  #appends content to file
f.close() 

f = open("demofile.txt", "w")                            #opens and lets you rewrite file
f.write("the contents of the file have been replaced")   #rewrites file
f.close()

import os
if os.path.exists("demofile.txt"):      #checks if file exists
    os.remove("demofile.txt")          #deletes it if it does
else:
    print("no file found")

os.rmdir("mydemofilefolder")           #deletes folder