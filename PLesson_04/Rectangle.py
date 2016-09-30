length = float(input("What is the length of your rectangle? "))
width = float(input("What is the width of your rectangle? "))
perimeter = (2 * length) + (2 * width)


def calcPerim(perimeter):
    return("{:100.5f}".format (perimeter))
  

print("Your rectangle is", perimeter, "sq ft around.")
