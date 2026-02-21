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

# center() method returns a centered string
print(str.center(30))
print(len(str.center(30))) # center method adds spaces to the left and right of the string to make it centered, so the length of the centered string will be 30
print(len(str))

# count() retun the number of times is present in string
print("The o string (letter) present in the number of : ",(str.count("o"))) # it will count the number of times "o" is present in the string

# endswith() is used to check the sreing endwith
str1 = "Hi gyus"
print(str1)
print("The us word (String) is end on the string on index ( 4 (Start) , 7 (End)) (True / False) :",str1.endswith("us", 4, 7))

# find() is used to finde the string is present or not and return index number of the first occurence
print("(find()): The index of 'an' in the string is:", name.find("an")) 

# index() is used to find the index of the string whist is present at the location
print("(index()): The index of 'an' in the string is:", name.index("an"))

# isalnum() is used to check the string is alphanumeric or not
print(name.isalnum()) # it will return the string is alphanumeric in true or false
# isalnum() it's check the string A_Z, a-z, 0-9

# isalpha() is used to check the string is alphabetic or not
print(name.isalpha()) # it will return the string is alphabetic in true or false
# isalpha() it's check the string A-Z, a-z

# islower() is used to check the string is lowercase or not
print(name.islower()) # it will return the string is lowercase in true or false