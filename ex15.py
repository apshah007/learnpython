
#imports a module
from sys import argv
# gets 2 variables from the user
script, filename = argv
#opens a file
txt = open(filename)
#writes to the screen about the filename
print(f"Here is your file {filename}:")
#reads from the file
print(txt.read())
#writes to the screen the file's name
print("type the filename again:")
#assigns variable to input
file_again = input ("> ")
#assigns a variable to open file
txt_again = open(file_again)
#prints what is read from txt_again to the screen
print(txt_again.read())
txt.close()
txt_again.close()
