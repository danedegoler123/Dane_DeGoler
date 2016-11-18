radius = float(input("Enter the radius of your circle: "))
area = (3.14 * (radius**2))


def calcArea():
    global radius
    area = (3.14 * (radius**2))

print("The area of a circle with a radius of", radius ,"is", area)
calcArea()
