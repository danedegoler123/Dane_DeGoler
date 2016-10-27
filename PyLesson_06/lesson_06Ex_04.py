integer = int(input("Please enter the integer that you would like to use: "))
sizeOfTable = int(input("Please enter the size of your table: "))

def table():
    print("   x-values \t result")
    print("----------------------------")
    for i in range(1, sizeOfTable+1, 1):
        print("\t", i,"\t", i*integer)

table()
