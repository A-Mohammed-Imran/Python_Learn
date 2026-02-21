# Match Statement

x = int(input("Enter a 1 to 4 number:"))

# match method is used to check the multiple conditions in a more elegant way than if-elif-else statement it's similar to switch case statement in other programming languages

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("three")
    case _:
        print("Invalid number")