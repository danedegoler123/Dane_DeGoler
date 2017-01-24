
import math
class Distance:
    #Constructor
    def __init__(self, x1="", y1="", x2="", y2=""):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        distance = 0

    #Modifier
    def setx1(self, newx1):
        self.xOne = newx1
    def sety1(self, newy1):
        self.yOne = newy1
    def setx2(self, newx2):
        self.xTwo= newx2
    def sety2(self, newy2):
        self.yTwo = newy2
        

    #Accessor
    def getxOne(self):
        return self.xOne
    def getyOne(self):
        return self.yOne
    def getxTwo(self):
        return self.xTwo
    def getyTwo(self):
        return self.yTwo
    def getDistance(self):
        self.distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne))
        return self.distance

def main():
    xOne = int(input("Enter the first input: "))
    yOne = int(input("Enter the second input: "))
    xTwo = int(input("Enter the third input: "))
    yTwo = int(input("Enter the fourth input: ")) 

    user1 = Distance(xOne, yOne, xTwo, yTwo)
    print("distance =",user1.getDistance())

    user1.setx1(1)
    user1.sety1(2)
    user1.setx2(3)
    user1.sety2(4)
    print("distance =",user1.getDistance())

main()

