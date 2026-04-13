# File io 


m1 = open("Apna college\\demo.txt", "r")
print("File is printing using readline method:")
l1 = m1.readline()
print(l1)
l2 = m1.readline()
print(l2)
m1.close()

m2 = open("Apna college\\demo.txt", "r")
data = m2.read()
print("File is printing on read mode:")
print(data)
m2.close()

m3 = open("Apna college\\demo.txt", "w")
print("File is printing on write mode:")
d = m3.write("This is a new line")
print(d)
m3.close()

m4 = open("Apna college\\demo.txt", "a")
print("File is printing on append mode:")
d1 = m4.write("\nThis is a new line")
print(d1)
m4.close()

with open("Apna college\\demo.txt", "r") as f:
    data3 = f. read()
    print(data3)

with open("Apna college\\demo.txt", "w") as f1:
    f1.write("new data")

# to delete a file we can use os module and its remove function. We have to pass the path of the file which we want to delete.
import os
os.remove("Apna college\\demo.txt")

with open("Apna college\\practice.txt", "w") as f2:
    f2.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
