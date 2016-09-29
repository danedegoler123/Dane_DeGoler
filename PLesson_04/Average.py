
one = float(input("Enter the first number: "))
two = float(input("Enter the second number: "))
three = float(input("Enter the third number: "))

def average(one, two, three):
    return("{:10.5f}".format ((one + two + three)/3)) 

print("The average of", one, two, three, "is", average(one, two, three))   

