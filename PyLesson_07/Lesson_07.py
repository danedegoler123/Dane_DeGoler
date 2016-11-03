number = int(input("Please enter a number: "))

while number > 0:
    # %10 returns the last digit on the right
    print(number %10)
    #dividing by 10 shaves of the last digit on the right
    number = int(number / 10)



##number = int(input("Please enter a number: "))
##digits = 0
##num = number
##
##while num > 0:
##    digits += 1
##    num = int(num /10) 
##
##print("There are", digits, "digits in", number)


##sentence = input("Please enter a String: ") 
##
##top = 0
##while top < sentence.count(" ") > 0:
##    sentence = sentence[0 : sentence.index(" ")] + sentence[sentence.index(" ")+1 : len(sentence)]
##
##print("Without spaces..." + sentence)    
