myList = ("one","two","three","four","five")
print("In order...")
output = ""
for i in myList:
    print(i)
output += i + " "
print(output)

print("\n")
print("Reversed...")
output = ""
for i in range(len(myList)-1, -1, -1):
    output += myList[i] + " "
print(output)




    
