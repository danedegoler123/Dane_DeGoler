height = int(input("Enter your height in inches: "))
weight = int(input("Enter your weight in pounds: "))

condition = (weight / (height * height)) * 703
bmi = 0

def calcBMI(condition):
    if condition < 18.5:
        print("You are underweight")

    elif condition <= 24.9:
        print("You are normal")

    elif condition <= 29.9:
        print("You are overweight")

    elif condition <= 34.9:
        print("You are obese")

    elif condition <= 39.9:
        print("You are very obese")

    if condition > 39.9:
        print("You are morbidly obese")

        
calcBMI(condition)

print("Your BMI is", condition)

