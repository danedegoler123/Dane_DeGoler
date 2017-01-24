import random
class User:
    #Constructor
    def __init__(self, fName, lName, avat = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0, 1000000)
        
    #Modifier
    def setfName(self, newfName):
        self.firstName = newfName
    def setlName(self, newlName):
        self.lastName = newlName
    def setavat(self, newavat):
        self.avatar = newavat

    #Accessor
    def getfirstName(self):
        return self.firstName
    def getlastName(self):
        return self.lastName
    def getavatar(self):
        return self.avatar
    def getuserID(self):
        return self.userID
    
    def __str__(self):
        return "Customer Info...\nFirst Name: " + self.firstName + \
                "\nLast Name: " + self.lastName + \
                "\nAvatar: " + self.avatar + \
                "\nUser ID#: " + str(self.userID)
def main():
    firstName = input("What would you like your first name to be? ")
    lastName = input("What would you like you last name to be? ")
    answer = input("Would you like to use a public avatar? y or n: ")

    if answer == "n":
        user1 = User(firstName, lastName)
    if answer == "y":
        avatar = input("Please enter your avatar's name: ")
        user1 = User(firstName, lastName, avatar)
    print(user1) 



main() 




