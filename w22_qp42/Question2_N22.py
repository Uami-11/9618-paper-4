class Character:
    def __init__(self, namep, Xcor, Ycor):
        self.__Name = namep
        self.__XCoordinate = Xcor
        self.__YCoordinate = Ycor

    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange

CharacterArray = []
try:
    file = open("Characters.txt", 'r')
    for i in range(10):
        CharName = file.readline().strip()
        Xpos = int(file.readline().strip())
        Ypos = int(file.readline().strip())
        CharWhole = Character(CharName, Xpos, Ypos)
        CharacterArray.append(CharWhole)
    file.close()
except IOError:
    print("Could not find file")
