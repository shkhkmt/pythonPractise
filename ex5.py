name = 'Mangaliso S. Ndabeni'
age = 31 # Not a lie 
height = 181 # centimeters 
weight = 90 # kgs 
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He weighs {weight} kilograms")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair. Obviously.")
print(f"His teeth are {teeth}, depending on the coffee.")

# this line is tricky, try to get it exactly right. 

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# converting variable's to pounds and inches. 

height_inches = height / 2.54 
weight_pounds = weight * 2.20462

print(f"His weight in pounds is {weight_pounds}. Not bad, huh?")
print(f"His height in inches is {height_inches}. He wishes he was a little bit taller.")