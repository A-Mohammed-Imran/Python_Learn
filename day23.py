faa = [6, 1, 2, 3]
print(faa)

faa.sort()
print(faa)

faa.append(4)
print(faa)

faa.sort()
print(faa)

m = faa.copy()
m[0] = 0     
print("another list :", m)     