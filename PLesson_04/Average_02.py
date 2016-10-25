one = float(input("Enter the first number: "))
two = float(input("Enter the second number: "))
three = float(input("Enter the third number: "))

def calcAverage():
    global average
    average =((one + two + three)/3) 

print("The average of", one, two, three, "is", "{:10.5f}".format((one + two + three)/3))    

calcAverage() 
