

import random
numbers= [] 
for i in range(0,10):
    numbers.append(random.randint(1,100))
print("Numbers...")


output = ""
for i in numbers:
    output += str(i) + " "
print(output)
print("\n")


def averaged():
    global average, numbers
    for i in numbers:
        average += (i)
    return (average/len(numbers)) 

average = 0
print("The average of the above numbers is...", averaged())



