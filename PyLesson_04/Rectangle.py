length = float(input("What is the length of your rectangle? "))
width = float(input("What is the width of your rectangle? "))



def calcPerim():
    global length, width
    perimeter = (2 * length) + (2 * width)
  

print("Your rectangle is", perimeter, "sq ft around.")

calcPerim() 
