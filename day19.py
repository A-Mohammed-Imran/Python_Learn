# Break and continue statement

print("Break Statement")

for i in range(12):
    print("5 x", i, "=", 5 * i)
    if (i == 8):
        print("The iterate breaks")
        break
    # the break statement when becoms condition tru's and exit from loop

print("Continue Statement")

for w in range(12):
    if (w == 5):
        print("The value of w is 5 so skip it")
        continue
    # It breaks the currentiteration and continue's the loop
    print("5 x", w, "=", 5 * w)