def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print(f"You have {cheeseCount} cheeses!")
    print(f"You have {boxesOfCrackers} crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
cheeseAndCrackers(20,30)

print("OR, we can use variable from our script:")
amountOfCheese = 10
amountOfCrackers = 50

cheeseAndCrackers(amountOfCheese, amountOfCrackers)

print("We can even do math inside too:")
cheeseAndCrackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheeseAndCrackers(amountOfCheese + 100, amountOfCrackers + 1000)

print("We can take inputs to our functions in the command line: ")
amountOfCheese = float(input())
amountOfCrackers = float(input())
print(f"You have {amountOfCheese} cheeses")
'''
This shows the different ways we can give a function i.e., cheeseAndCrackers.py the values it needs to print them.

You can parse numbers, variables, and do math. Or combine the latter two.
'''
