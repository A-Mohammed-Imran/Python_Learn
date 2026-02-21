# Exersise 

import time 

timemap = time.strftime("%H,%M,%S")
print(timemap)

timeof = time.strftime("%H")

print(type(timeof))

if (0 <= int(timeof) < 11) : 
    print("Good Morning")
elif (11 <= int(timeof) < 17) :
    print("Good Afternoon")
else :
    print("Good Evening")