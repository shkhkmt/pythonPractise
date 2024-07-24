# this one is like your scrips with argv

def printTwo(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

''' The args is actually pointless, we can just do this. (when you use def like this, you name the code block and then call it using args i.e., it's a script that print's 2 arguments'''

def printTwoAgain(arg1, arg2):
    print(f"arg:1 {arg1}, arg2: {arg2}")

# this just takes one argument

def printOne(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments

def printNone():
    print("I got nothin'.")

printTwo("Mangaliso", "Ndabeni")
printTwoAgain("Mangaliso", "Ndabeni")
printOne("First!")
printNone()
