# Desistion Making State Ment

age = int(input("Enter Your age : "))

# if , elif , else statement 

if (age > 18):# if check the condition is true or false if it's true the the condition will run if false the move to next statement 
    print("You can't drive")

elif (age == 18): # elif is used to check the another condition if the first condition is false and the elif condition is true then the elif block will run
    print("You can drive but with the supervision of an adult")

# else execute when the if and elif condition is false
else:
    print("You can drive")

print("Ower desition is finaled")

# nested if statement
# Nested if statement is a if statement inside another if statement where we can check multiple conditions 

b = int(input("Enter the number : "))
if (b > 0):
    print("The number is positive")
    if (b % 2 == 0):
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative")