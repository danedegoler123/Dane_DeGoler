length = float(input("What is the length of your rectangle? "))
width = float(input("What is the width of your rectangle? "))
perimeter = (2 * length) + (2 * width)


def calcPerim():
    global perimeter
    perimeter = (2 * length) + (2 * width)

print("Your rectangle is", "{:10.5f}".format(perimeter), "sq ft around.")

calcPerim()
