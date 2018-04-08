# imports the module argv
from sys import argv
# asks for arguments when the program is started
script, input_file = argv
# defines a function
def print_all(f):
    print(f.read())
# defines a function
def rewind(f):
    f.seek(0)
# defines a function
def print_a_line(line_count, f):
    print(line_count, f.readline())
#sets a variable equal to the contents of the open file
current_file = open(input_file)

#prints a statement to the screen
print("first lets print the whole file:\n")
# prints all information to the current file
print_all(current_file)
#prints to the screen
print("Now lets rewind, kind of like tape.")
# calls function rewind
rewind(current_file)
#prints the 3 lines of the test.txt file to the screen
print ("Lets print 3 lines:")

#starts with line one
current_line = 1
#uses a function to print a line
print_a_line(current_line, current_file)
# uses a function to print a line
# jump down to the following line to print that using the function
current_line = current_line +1
print_a_line(current_line, current_file)
# the following code is the same only goes down to the third line 

current_line = current_line +1
print_a_line(current_line, current_file)
