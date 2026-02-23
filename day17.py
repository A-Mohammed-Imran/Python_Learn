# Itreative Statement 

# for loop

names = ["imran", "azhan", "sufiyan"]
for name in names:
    print(name)
    # the new variable name is only for the loop and it will not change the original variable names
    for i in name:
        print(i)
        # Again the new variable i is only for the loop and it will not change the original variable name

# range method is used to iterate a sequence of numbers
for i in range(5):
    print(i+1)

# (Start, Stop, Step)
for w in range(1, 20, 4):
    print(w)

