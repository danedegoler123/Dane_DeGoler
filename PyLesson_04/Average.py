one = float(input("Enter the first number: "))
two = float(input("Enter the second number: "))
three = float(input("Enter the third number: "))

def average():
    global one, two, three
    average = ((one + two + three)/3)
    

print("The average of", one, two, three, "is", average)   

average() 
