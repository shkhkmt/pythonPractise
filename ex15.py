from sys import argv

# using argv to get a filename.
 
script, filename = argv
txt = open(filename)

#using open() function to is better than input bc you don't need to type the correct file name twice
# printing the filename and reading then printing its content to the terminal

print(f"Here's your file {filename}:")

#calling a funtion (read) on the file .txt

print(txt.read())

'''
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

txt_again = open(file_again)

print(txt_again.read())

'''

# When you use a print statement to open the file, you'll need to 
# input the name of the file correctly. 
