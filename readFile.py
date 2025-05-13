from sys import argv

#using argv to get a file (also specifying the number of arguments in the script)

script, fileName = argv

#reading the content of the text file

txt = open(fileName)

#printing the contents of the text file into the terminal

print(f"Here are the contents of {fileName}:")
print(txt.read())
