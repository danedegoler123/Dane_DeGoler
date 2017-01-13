class MilesPerHour:
    #Constructor
    def __init__(self, dist="", hrs="", mins=""):
        self.distance = dist
        self.hours = hrs
        self.minutes = mins
        mph =0
    #Modifier
    def setDist(self, newDist):
        self.distance = newDist
    def setHrs(self, newHrs):
        self.hours = newHrs
    def setMins(self, newMins):
        self.minutes= newMins
        
    #Accessor
    def getDistance(self):
        return self.distance
    def getHours(self):
        return self.hours
    def getMinutes(self):
        return self.minutes
    def getMph(self):
        self.mph = self.distance/(self.hours + self.minutes/60)
        return self.mph

def main():
    distance = int(input("Enter distance: "))
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))

    user1 = MilesPerHour(distance, hours, minutes)

    
    print("Distance:", user1.getDistance(),"miles")
    print("Time: ", user1.getHours()," hours and", user1.getMinutes(),"minutes")
    print("Speed: ", user1.getMph(),"miles per hour")

    user1.setDist(20)
    user1.setHrs(5) 
    user1.setMins(0)

    distance = int(input("Enter distance: "))
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))

    user2 = MilesPerHour(distance, hours, minutes)
    
    print("Distance:", user2.getDistance(),"miles") 
    print("Time: ", user2.getHours(),"hours and", user2.getMinutes(),"minutes")
    print("Speed: ", user2.getMph(),"miles per hour")

    user2.setDist(10)
    user2.setHrs(2) 
    user2.setMins(3)

main() 
