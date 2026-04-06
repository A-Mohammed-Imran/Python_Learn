# Finally Keyword

# The finally block is used to execute code that must be executed regardless of whether an exception is raised or not. It is typically used for cleanup actions, such as closing files or releasing resources.

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: ") )
        print(l[i])
        return 1
    except :
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed")
        # Ørint("I am always executed" )

x = func1()
print(x)