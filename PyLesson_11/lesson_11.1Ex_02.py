
class Human:
    #Constructor
    def __init__(self, h="", e="", s=""):
        self.hair = h
        self.eyes = e
        self.skin = s

    #Modifier
    def seth(self, newh):
        self.hair = newh
    def sete(self, newe):
        self.eyes = newe
    def sets(self, news):
        self.skin = news

    #Accessor
    def getHair(self):
        return self.hair
    def getEyes(self):
        return self.eyes
    def getSkin(self):
        return self.skin

def main():
    hair = input("Enter your hair color: ")
    eyes = input("Enter eye color: ")
    skin = input("Enter skin color: ")

    user1 = Human(hair, eyes, skin)
    print("My info...")
    print("Hair: ", user1.getHair())
    print("Eyes: ", user1.getEyes())
    print("Skin: ", user1.getSkin())

    user1.seth("blonde")
    user1.sete("blue")
    user1.sets("white")
    print("Friend's info...")
    print("Hair: ", user1.getHair())
    print("Eyes: ", user1.getEyes())
    print("Skin: ", user1.getSkin())

main()
    

