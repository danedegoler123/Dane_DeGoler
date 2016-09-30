side = float(input("Enter the length of the one of the sides of the cube: "))
sa = (6 * (side**2))

def calcSurf():
   global surfaceArea
   sa = (6 * (side**2))

print("The surface area of a cube with", side ,"sides is", "{:10.5f}".format(sa))   
