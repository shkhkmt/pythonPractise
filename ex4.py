# Creating known variables and assigning values to them.
cars = 100
spaceInACar = 4.0
drivers = 30
passengers = 90

# Creating the unknown variables and creating operations to calculate them

carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInACar
averagePassengersPerCar = passengers / carsDriven

# Printing the console output

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", carsNotDriven, "empty cars today.")
print("We can transport", carpoolCapacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", averagePassengersPerCar, "in each car.")
