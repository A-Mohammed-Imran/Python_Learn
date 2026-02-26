# Functuion aregument

# Default argument

def add(a=4, b=6):
    print(a + b)

add(3, 6)

def prinname(fname, midname="Mohammed", lastname = "Imran"):
    print(f"hello, {fname} {midname} {lastname}")

prinname("A")

def ave(*numbers):
    sum = 0;
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

print(ave(1, 2, 3))