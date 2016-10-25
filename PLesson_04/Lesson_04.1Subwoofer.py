height = int(input("Enter the height of your object in inches: "))
length = int(input("Enter the length of your object in inches: "))
width = int(input("Enter the width of your object in inches: ")) 

cubicInches = height * length * width

volume = cubicInches/1728

def subwoofer():
    print("Your subwoofer box is", cubicInches ," cubic inches.")

def calcVol():
    print("Your subwoofer box is", volume ,"cubic feet.")
    
subwoofer()
calcVol()
