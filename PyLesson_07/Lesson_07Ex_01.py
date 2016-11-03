
number = int(input("Please enter a number: "))
sum = int(0)
num = int(number)

def sumDigits(num,sum):
    while num > 0:
        sum = sum + (num % 10)
        num = int(num / 10)
    return sum

print("The sum of the digits in", number ,"is", sumDigits(num,sum)) 

