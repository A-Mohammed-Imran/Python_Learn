# String Methods

name = "imran"

print(name.upper()) # it will convert the string to upper case
print(name.lower()) # it will convert the string to lower case

# the rstrip() method removes any trailing characters (characters at the end of a string), space is the default trailing character to remove.

con = "lorem ipsum dolor sit amet, !!!!!!!!!!!!."
print(con.rstrip("!.")) # it will remove the trailing ! and . from the string

# Replace method

print(con.replace("lorem", "hello")) # it will replace "lorem" with "hello"

# split() is a mwth tha makes a string into list 
var = "A Mohammed Imran"
print(var.split(" ")) # it will split the string into list

# caplitalize() method converts the first character of string to uppercase
str = "lorem ipsum dolor sit amet"
print(str.capitalize()) # it will convert's first character to uppercase
