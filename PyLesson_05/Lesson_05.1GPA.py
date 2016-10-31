
grade1 = input("Enter the letter grade for your first class: ")
grade2 = input("Enter the letter grade for your second class: ")
grade3 = input("Enter the letter grade for your third class: ")
grade4 = input("Enter the letter grade for your fourth class: ")
grade5 = input("Enter the letter grade for your fifth class: ")
grade6 = input("Enter the letter grade for your sixth class: ")
grade7 = input("Enter the letter grade for your seventh class: ")

def calcPoints(grade):
    if grade == "A":
        return 4.0
    if grade == "B":
        return 3.0
    if grade == "C":
        return 2.0
    if grade == "D":
        return 1.0
    if grade == "F":
        return 0.0

calcPoints(grade1)
calcPoints(grade2)
calcPoints(grade3)
calcPoints(grade4)
calcPoints(grade5)
calcPoints(grade6)
calcPoints(grade7)

gpa = (calcPoints(grade1) + calcPoints(grade2) +calcPoints(grade3) +calcPoints(grade4) + calcPoints(grade5) + calcPoints(grade6) + calcPoints(grade7))/7
                                                                                                                                       
print("Your GPA is", gpa)

