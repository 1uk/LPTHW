# defining the number of cars
cars = 100
# defingin the space in a car
space_in_a_car = 4.0
# defining the number of drivers
drivers = 30
# defining the number of passengers
passengers = 90
# calculating and defining the number of cars not driven
cars_not_driven = cars - drivers
# defining the number of cars driven
cars_driven = drivers
# calculating and defining the carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# calculating and defining the average passengers per car
average_passengers_per_car = passengers / cars_driven


# printing the whole stuff
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
