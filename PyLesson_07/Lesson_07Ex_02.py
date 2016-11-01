number = int(input("Please enter a number: "))
digits = 0
average = 0
num = number

def avDigits (num, average, digits):
    while num > 0:
        digits += 1
        average += num % 10
        num = int(num / 10)
    average /= digits
    return average
print("The average digits in", number ,"is", avDigits(num, average, digits)) 




