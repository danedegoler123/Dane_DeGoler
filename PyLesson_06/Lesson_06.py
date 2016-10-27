#PRINTING NUMBER RANGE (INCREASE BY 1)
##for i in range(1,5):
##    print(i) 


#PRINTING NUMBER RANGE (DECREASE BY 2 EACH TIME)
##for i in range(10,2,-2):
##    print(i) 



##output = ""
##for i in range(1,11):
##    output = output + str(i) + " "
##print(output) 


#EXAMPLE
##need = int(input("Please enter the number of cookies that you need: "))
##batchSize= 25
##batch = 1
##for cookies in range(need, -1, -batchSize):
##    print("Cookies Needed: ", cookies)
##    print("Batch #: ", batch)
##    batch = batch + 1
##
##print("Order up!!")



#NUMBER OF LETTERS
##word = "COMPSCI"
##print(len(word))



#HOW MANY SPACES UNTILL LETTER
##word = "COMPSCI"
##print(word.index("S")) 



#PRINTING WORD WITH A RANGE
##word = "COMPSCI"
##print(word[1:4])


#PRINTING WORD VERTICALLY
##word = input("Please enter a word: ")
##
##for i in range (0, len(word)):
##    print(word[i]) 



word = input("Please enter a word: ")
def printTri():
    for i in range(0,len(word)+1):
        print(word[0:i])
printTri()
        
