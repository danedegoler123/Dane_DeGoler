side = float(input("Enter the length of the one of the sides of the cube: "))
sa = (6 * (side**2))

def calcSurf(sa):
    return("{:10.5f}".format(sa))

print("The surface area of a cube with", side ,"sides is", sa)    
