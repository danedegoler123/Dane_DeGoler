number = int(input("Please enter a number: "))
rev = 0

def getReverse():
    global rev
    num = number
    while num > 0:
        rev = rev * 10
        rev += num % 10
        num = int(num/10)

getReverse() 
print(number,"reversed is",rev) 


        
        
