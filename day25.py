#  Tupe operations

t = (1, "a", 2, "b", 3);

print(t)
print(type(t))

l = list(t)

print(l)
print(type(l))
l.append(4)
l.pop(0)
l[3] = "c"

print(l)

nt = tuple(l)

print(nt)
print(type(nt))

l1 = (1, 2, 3)
l2 = (4, 5 , 6, 7)

l3 =l1 + l2

print(l3)

# methods 

let= (1, 2, 3, 4, 5)

print(let.count(2))
print(let.index(3))