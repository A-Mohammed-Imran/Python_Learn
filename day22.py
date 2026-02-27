# List Data type

l = [1, 2, 3]
print(l)
print(type(l))

le = [1, 3, True, "By"]
for i in le:
    print(i, type(i))

if True in le:
    print(True)

if "y" in "by":
    print("Y in List")