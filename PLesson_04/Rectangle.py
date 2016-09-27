length = float(input("What is the lenghth of your rectangle? "))
width = float(input("What is the width of your rectangle? "))
perimeter = (2 * length) + (2 * width)


def calcPerim(perimeter):
    print("{:100.5f}".format (perimeter))
  

print("Your rectangle is", perimeter, "sq ft around.")
