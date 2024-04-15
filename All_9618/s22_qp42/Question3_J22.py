class Card:
    def __init__(self, numberp, colourp):
        self.__Number = numberp
        self.__Colour = colourp

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

CardArray = [0] *30
try:
    file = open("CardValues.txt", 'r')
    for i in range(30):
        number = int(file.readline().strip())
        colour = file.readline().strip()
        CardArray[i] = Card(number, colour)

    file.close()
except IOError:
    print("file not found.")

NumbersChosen = [0]
def ChooseCard():
    global NumbersChosen

    CardIndex = 0
    while (CardIndex < 1 or CardIndex > 30) or (CardIndex in NumbersChosen):
        CardIndex = int(input("Enter card to choose: "))
        if CardIndex in NumbersChosen:
            print("Card already selected.")
        elif (CardIndex < 1 or CardIndex > 30):
            print("Card does not exist.")

    NumbersChosen.append(CardIndex)
    CardIndex = CardIndex - 1
    return CardIndex

Player1 = []
for i in range(4):
    OneCard = ChooseCard()
    Player1.append(CardArray[OneCard])


for i in range(4):
    print("Card"+str(i+1)+"'s Number: "+ str(Player1[i].GetNumber()) +"\n"+
          "Card"+str(i+1)+"'s colour: "+ str(Player1[i].GetColour()))
