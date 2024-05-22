class Character:
    def __init__(self, namep, xpos, ypos):
        self.__Name = namep
        self.__XPosition = xpos
        self.__YPosition = ypos

    def GetXPosition(self):
        return self.__XPosition
    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, NewPos):
        self.__XPosition += NewPos
        if self.__XPosition > 10_000:
            self.__XPosition = 10000
        if self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self, NewPos):
        self.__YPosition += NewPos
        if self.__YPosition > 10_000:
            self.__YPosition = 10000
        if self.__YPosition < 0:
            self.__YPosition = 0

    def Move(self, movement):
        if movement == "up":
            self.SetYPosition(10)
        if movement == "down":
            self.SetYPosition(-10)
        if movement == "left":
            self.SetXPosition(-10)
        if movement == "right":
            self.SetXPosition(10)

Character1 = Character("Jack", 50, 50)

class BikeCharacter(Character):
    def __init__(self, namep, xpos, ypos):
        super().__init__(namep, xpos, ypos)

    def Move(self, movement):
        if movement == "up":
            self.SetYPosition(20)
        if movement == "down":
            self.SetYPosition(-20)
        if movement == "left":
            self.SetXPosition(-20)
        if movement == "right":
            self.SetXPosition(20)
        

Bike1 = BikeCharacter("Karla", 100, 50)

chara = ""
while (chara != "jack") and (chara != "karla"):
    chara = input("Enter which character to move: ").lower()
    if (chara != "jack") and (chara != "karla"):
        print("Invalid Character.")

move = ""
while (move != "up") and (move != "down") and (move != "left") and (move != "right"):
    move = input('Enter the direction to move: ').lower()
    if (move != "up") and (move != "down") and (move != "left") and (move != "right"):
        print("Invalid Direction.")

if chara == "jack":
    Movement = Character1.Move(move)
    Xpos = Character1.GetXPosition()
    Ypos = Character1.GetYPosition()
else:
    Movement = Bike1.Move(move)
    Xpos = Bike1.GetXPosition()
    Ypos = Bike1.GetYPosition()

print(chara, "'s new position is X = ", Xpos, " Y = ", Ypos)