radius = float(input("Enter the radius of your circle: "))
area = (3.14 * (radius**2))


def calcArea(area):
    return("{:10.5f}".format(area))

print("The area of a circle with a radius of", radius ,"is", area)

calcArea(area)
