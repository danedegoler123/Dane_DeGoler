
class Car:
    #Constructor
    def __init__(self, p="", i="", e="", t=""):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    #Modifier
    def setp(self, newp):
        self.paint = newp
    def seti(self, newi):
        self.interior = newi
    def sete(self, newe):
        self.engine = newe
    def sett(self, newt):
        self.tires = newt

    #Accessor
    def getPaint(self):
        return self.paint
    def getInterior(self):
        return self.interior
    def getEngine(self):
        return self.engine
    def getTires(self):
        return self.tires

def main():
    paint = input("Enter your paint color: ")
    interior = input("Enter the type of interior: ")
    engine = input("Enter the type of engine: ")
    tires = input("Enter the type of tires: ")

    user1 = Car(paint, interior, engine, tires)
    print("Your vehicle is ready.....")
    print("Paint: ", user1.getPaint()) 
    print("Interior: ", user1.getInterior())
    
    print("Engine: ", user1.getEngine())
    print("Tires: ", user1.getTires())

    user1.setp("red with gold fleck")
    user1.seti("Corinthian leather (brown)") 
    user1.sete("5 litre v8 507hp")
    user1.sett("20 inch Priellis") 
    print("The vehicle is ready.....")
    print("Paint: ", user1.getPaint()) 
    print("Interior: ", user1.getInterior())
    print("Engine: ", user1.getEngine())
    print("Tires: ", user1.getTires())
    


main()     

