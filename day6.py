# variables
# that can hold different types of data

a = 123456 
b = "Hello world"
c = True
d = None

print(a, b, c, d)

# **** Data types in python ****

# 1 Numeric data type : int, float, complex
a = 123456 # integer data type
b = 123.456 # float data type
c = 1 + 2j # complex data type
print(a,b,c)
print(type(a), type(b), type(c))

# 2 Text data type : str
a = "Hello world" # string data type
print(type(a))

# 3 Boolean data type : bool
a = True # boolean data type
b = False # boolean data type
print(a,b)
print(type(a), type(b))

# 4 None data type : None
a = None # None data type
print(a)
print(type(a))

# 5 List data type : list
a = [1, 2, 3, 4, 5] # list data type
print(a)
print(type(a))

# 6 Tuple data type : tuple
a = (1, 2, 3, 4, 5) # tuple data type
print(a)
print(type(a))

# 7 Set data type : set
a = {1, 2, 3, 4, 5} # set data type
print(a)
print(type(a))

# 8 Dictionary data type : dict
a = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"} # dictionary data type
print(a)
print(type(a))

# Combining all data types
a = 123456 # integer data type
b = "Hello world" # string data type
c = True # boolean data type   
d = None # None data type
e = [1, 2, 3, 4, 5] # list data type
f = (1, 2, 3, 4, 5) # tuple data type
g = {1, 2, 3, 4, 5} # set data type
h = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"} # dictionary data type

print(a, b, c, d, e, f, g, h)

print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))