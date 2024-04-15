class Balloon:
    def __init__(self, colourp, defencep):
        self.__Health = 100
        self.__Colour = colourp
        self.__DefenceItem = defencep

    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self, Heealthp):
        self.__Health += Heealthp

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False

Item = input("Enter the defence item: ")
Colour = input("Enter the colour of the balloon: ")
Balloon1 = Balloon(Colour, Item)

def Defend(Ballons):
    strength = int(input("Enter opponent's strength: "))
    Ballons.ChangeHealth(-strength)
    print("The defence item: " + str(Ballons.GetDefenceItem()))
    Popped = Ballons.CheckHealth()
    if Popped:
        print("Defence not succeded.")
    else:
        print("succesess")

    return Ballons
Balloon1 = Defend(Balloon1)