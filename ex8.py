# formatter is a variable that accepts 4 inputs. 

formatter = "{} {} {} {}"

# calling inputs to formatter then printing them out as strings. 

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))

#caling strings into the formater. 
print(formatter.format(
      "Wo mathambo,", 
      "wo mathambo.", 
      "Hlanganani.",
      "Wo mthambo hlanganani"
      ))