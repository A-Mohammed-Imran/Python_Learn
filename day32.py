# All common set operations

se1 = {1, 2, 3, 4, 5}
se2 = {4, 5, 6, 7, 8}

print("se1:", se1)
print("se2:", se2)

# 1) Union
print("\nUnion (se1 | se2):", se1.union(se2))
u = se1.copy()
u.update(se2)  # in-place union
print("Update (in-place union):", u)

# 2) Intersection
print("\nIntersection (se1 & se2):", se1.intersection(se2))
i = se1.copy()
i.intersection_update(se2)  # in-place intersection
print("Intersection update (in-place):", i)

# 3) Difference
print("\nDifference (se1 - se2):", se1.difference(se2))
d = se1.copy()
d.difference_update(se2)  # in-place difference
print("Difference update (in-place):", d)

# 4) Symmetric difference
print("\nSymmetric difference (se1 ^ se2):", se1.symmetric_difference(se2))
sd = se1.copy()
sd.symmetric_difference_update(se2)  # in-place symmetric difference
print("Symmetric difference update (in-place):", sd)

# 5) Relation checks
print("\nIs subset? se1 <= se2:", se1.issubset(se2))
print("Is superset? se1 >= se2:", se1.issuperset(se2))
print("Is disjoint? se1 and se2:", se1.isdisjoint(se2))

# 6) Basic element methods
basic = se1.copy()
basic.add(10)
print("\nAfter add(10):", basic)
basic.remove(10)
print("After remove(10):", basic)
basic.discard(99)  # no error even if element not found
print("After discard(99):", basic)
removed = basic.pop()  # removes an arbitrary element
print("After pop():", basic, "| removed:", removed)

temp = se2.copy()
temp.clear()
print("After clear() on copy of se2:", temp)

