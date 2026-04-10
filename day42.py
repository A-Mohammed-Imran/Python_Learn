# Enumarate function

a = [1, 2, 3, 4, 5, 6, 7]
for index, net in enumerate(a):
    print(net)
    if net == 4:
        print(f"Index of 4 is {index}")

# The enumerate() function adds a counter to an iterable and returns it in a form of enumerating object. This enumerated object can then be used directly in for loops or be converted into a list of tuples using the list() method. The syntax is as follows:

# Kay bi na ba dak yu ea variable a usa iterate kar ta hai aur uska index bhi chahiye to hum enumerate function ka use kar sakte hai. Enumerate function iterable object ke sath index bhi return karta hai.