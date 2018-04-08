#define a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes_of_crackers!")
    print("Man thats enough for a party!")
    print("get a blanket.\n")

#hard coded info
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
#use a variable to put into arguments for a function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#calling a function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#printing some info to the screen then calling the function
print("we can even do math inside too:")
cheese_and_crackers(10+20, 5+6)
#using math operators to add to the variables to pass to the cheese_and_crackers function 
print("and we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers +1000)
