# Raising an custom error

a = int(input("Enter the age: "))
if(a<=18):
    raise ValueError("Age must be greater than 18")
else:
    print("You are eligible to vote") 