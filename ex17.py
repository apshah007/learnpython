# imports these modules
from sys import argv
from os.path import exists
#starts the program by getting the needed info
script, from_file, to_file = argv
# tells the use that we are copying from one file to another
print(f"Copying from {from_file} to {to_file}")
# we could do these two on one line how?
# open from file to read from it
in_file = open(from_file)
indata = in_file.read()
# print how long the input file is
print(f"The input file is {len(indata)} bytes long")
# print if the output file exist
print(f"Does the output file exist? {exists(to_file)}")
#prints to screen a message
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
# recieves input from input prompt
input ()
#opens the file to write to
out_file = open(to_file, 'w')
#writes to the file
out_file.write(indata)
#prints to screen that the writing is completed
print("Alright, all done.")
#closes both files 
out_file.close()
in_file.close()
