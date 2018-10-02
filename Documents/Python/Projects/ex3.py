#this is the number of cars
cars = 100
#this is the space in a car
space_in_a_car = 4
#this is the amount of driver
drivers = 30
#this is the amount of passangers
passangers = 90
#this is the amount of cars not driven today
cars_not_driven = cars - drivers
#these are the cars being driven today
cars_driven = drivers

#this is the capacity available for carpooling
carpool_capacity = cars_driven * space_in_a_car

#this is the average passengers per car if we were to carpool everybody!!!
average_passengers_per_car = passangers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We need to put about", average_passengers_per_car, " in each car")