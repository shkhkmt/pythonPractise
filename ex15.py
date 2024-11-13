from sys import argv

# using argv to get a filename.

script, fileName = argv
txt = open(fileName)

#using open() function to is better than input bc you don't need to type the correct file name twice
# printing the filename and reading then printing its content to the terminal

print(f"Here's your file {fileName}:")

#calling a funtion (read) on the file .txt

print(txt.read())

'''
print("Type the filename again:")

fileAgain = input("> ")

txtAgain = open(fileAgain)

txtAgain = open(fileAgain)

print(txtAgain.read())
'''

# When you use a print statement to open the file, you'll need to
# input the name of the file correctly.

#This script reads the content of a file and then outputs it in the terminal
