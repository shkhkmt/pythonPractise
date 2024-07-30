from sys import argv
# importing script, "input file" from argv
script, inputFile = argv
#defining the function printAll and calling the module f.read to read the full text.
def printAll(f):
    print(f.read())
#defining the function rewind to read f again. f.seek to go back to the beginning of the file
def rewind(f):
    f.seek(0)
#defining the function print line, that reads the lineCount using f.readline()
def printLine(lineCount, f):
    print(lineCount, f.readline())

currentFile = open(inputFile)

print("First let's print the whole file:\n")

printAll(currentFile)

print("Now let's rewind, kind of like a tape.")

rewind(currentFile)

print("Let's print three lines: ")

currentLine = 1
printLine(currentLine, currentFile)

currentLine += 1
printLine(currentLine, currentFile)

currentLine += 1
printLine(currentLine, currentFile)
