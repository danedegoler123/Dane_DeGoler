side = float(input("Enter the length of the one of the sides of the cube: "))


def calcSurf():
    global side
    sa = (6 *(side**2)) 

print("The surface area of a cube with", side ,"sides is", sa)    

calcSurf() 
