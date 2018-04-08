
# imports the argv module
from sys import argv
# asks for the 2 arguments when the program is started
script, filename = argv
# prints to the screen certain commands
print (f"We're going to erase {filename}.")
print ("if you dont want that, hit CTRL-C (^C).")
print ("if you do want that, hit RETURN.")
# asks for an input
input("?")
#prints that you are opening the file to the screen
print("Opening the file...")
#opens the file for writing and stores it in a variable target
target = open(filename, 'w')
#prints the statement that the file will be deleted
print ("Truncating the file.  Goodbye!")
# deletes the file
target.truncate()
#asks for new data for the file
print("Now I'm going to ask you 3 lines")
#asks for data for 3 lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
#prints to the screen a statement
print("im going to write these to the file.")
#writes to the text file the new information
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# prints a statement to the screen
print("And finally, we close it.")
# closes the file and no longer writes in it
target.close()
