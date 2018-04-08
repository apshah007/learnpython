
# intially assigns the variables to a value
people = 30
cars = 40
trucks = 15

# different case scenarios - if cars is greater than people, the print
if cars > people:
    print("We should take the cars.")
# if cars is less than people then print
elif cars < people:
    print("we should not take the cars.")
# if cars is not greater than or equal to people then print
else:
    print("we cant decide")

# different case scenarios - if trucks is greater than cars print
if trucks > cars:
    print("thats too many trucks")
# if trucks is less than cars then print
elif trucks < cars:
     print("Maybe we could take the trucks.")
# if neither case then print
else:
    print("we still cant decide.")
# if people are greater than trucks then print
if people > trucks:
    print("Alright, lets just take the trucks")
# if people are less than trucks then print
else:
    print("Fine, lets stay home then.")


#if multiple elif blocks are true, python starts at the top and runs the first
# block that is true, so that it will only run the first one 
