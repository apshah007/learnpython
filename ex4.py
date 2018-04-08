
# there are 100 cars
cars = 100

# there is space for 4 in a car
space_in_a_car = 4

#there are 30 drivers
drivers = 30

#there are 90 passengers
passengers = 90

# this calculates the cars that are not driven
cars_not_driven = cars - drivers

#this equates the cars driven to the number of drivers
cars_driven = drivers
#the carpool capacity is the number of cars driven times the space in a car
carpool_capacity = cars_driven * space_in_a_car
#average passengers per car is total passengers divided by the number of cars
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
