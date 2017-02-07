
import random
class object1:
    #Constructor
    def __init__(self, manu="", n="", c="", p=""):
        self.manufacturer = manu
        self.name = n
        self.category = c
        self.price = p
        self.UPC = random.randint(0,100000000)

    #Modifier
    def setManu(self, newManu):
        self.manufacturer = newManu
    def setN(self, newN):
        self.name = newN

    #Accessor
    def getManufacturer(self):
        return self.manufacturer
    def getName(self):
        return self.name
    def getCategory(self):
        return self.category
    def getPrice(self):
        return self.price
    def getUPC(self):
        return self.UPC

    def __str__(self):
        return "Item info...\nName: " + self.name + \
               "\nManufacturer: " + self.manufacturer + \
               "\nCategory: " + self.category + \
               "\nPrice: " + self.price + \
               "\nUPC#: " + str(self.UPC)
def main():
    name = input("Enter the name: ")
    manufacturer = input("Enter the manufacturer: ")
    c = input("Will you be entering the category and price information? y or n: ")
    if c == "n":
        item1 = object1(manufacturer, name)
    if c == "y":
        category = input("Enter the category: ")
        price = int(input("Enter the price: ")) 
        item1 = object1(manufacturer, name, category, str(price))
    print(item1)

main()



