# Recursion

# let see an example of recusion 

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(1))

# Fibunachhi series

def feb(f):
    if (f == 0 or f == 1):
        return 1
    else:
        return feb(f-1) + feb(f-2)

n = int(input("Enter the number of febunatchhi series you want: "))
print(f"The Febunatchhi series of {n} is = {feb(n)}")