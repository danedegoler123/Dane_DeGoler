#CREATING LISTS IN PYTHON
myList = [1, 2, 3, 4, 5]

print(myList[2]) 
print(myList[:2])
print(myList[2:3]) 
print(myList) 


output = ""
j = 0
for i in myList:
    output += str(i)
    if j < len(myList)-1:
        output += ", "
    j += 1    
print(output)      



output = ""
for i in myList:
    output += str(i)
print(output)     




#ADDING VALUES TO YOUR LISTS
myList = []
myList.append("a")
myList.append(3)
myList.append("**&")
print(myList)


myList = []
for i in range (0,8):
    myList.append(i*4)

output = ""
j = 0
for i in myList:
    output += str(i)
    if j < len(myList):
        output += ", "
    j += 1

print(output)    



#USING THE SPLIT() FUNCTION
word = "P r o f e s s o r"
myList = word.split(" ")

print(myList)
for i in myList:
    output += (i)

print(output)    
