#Declarig variable and calling it into a sting. 

types_of_people = 10
x = f"There are {types_of_people} types of people"

#Initiating 2 stings and then putting them inside a string. 
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #sting in string 

#Printing strings from above. 

print(x)
print(y)

print(f"I said: {x}")

#initiating strings and then priting them

hilarious = False 
joke_evaluation = "Isn't that joke so funny!? {}" #string in string 

print(joke_evaluation.format(hilarious)) #string in string 

w = "This is the left side of..."
e = "a string whith a right side"

print(w + e) #string in string 

# w + e makes a longer string by adding the two strings together. 