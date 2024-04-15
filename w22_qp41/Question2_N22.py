class Card:
    def __init__(self, numberp, colourp):
        self.__Number = numberp
        self.__Colour = colourp

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

r1 = Card(1, "red")
r2 = Card(2, "red")
r3 = Card(3, "red")
r4 = Card(4, "red")
r5 = Card(5, "red")
b1 = Card(1, "blue")
b2 = Card(2, "blue")
b3 = Card(3, "blue")
b4 = Card(4, "blue")
b5 = Card(5, "blue")
y1 = Card(1, "yellow")
y2 = Card(2, "yellow")
y3 = Card(3, "yellow")
y4 = Card(4, "yellow")
y5 = Card(5, "yellow")

class Hand:
    def __init__(self, c1, c2, c3, c4, c5):
        self.__Cards = []
        self.__Cards.append(c1)
        self.__Cards.append(c2)
        self.__Cards.append(c3)
        self.__Cards.append(c4)
        self.__Cards.append(c5)
        self.__FirstCard = 0
        self.__NumberCards = 5

    def GetCard(self, pos):
        return self.__Cards[pos]

Player1 = Hand(r1, r2, r3, r4, y1)
Player2 = Hand(y2, y3, y4, y5, b1)

def CalculateValue(Hands):
    Score = 0
    for i in range(5):
        CardGot = Hands.GetCard(i)
        Colour = CardGot.GetColour()
        Number = CardGot.GetNumber()
        if Colour.lower() == "red":
            Score += 5
        elif Colour.lower() == "blue":
            Score += 10
        elif Colour.lower() == "yellow":
            Score += 15

        Score += Number
    return Score


OneScore = CalculateValue(Player1)
TwoScore = CalculateValue(Player2)
if OneScore > TwoScore:
    print("Player One Wins!")
elif TwoScore > OneScore:
    print("Player Two Wins!")
else:
    print("Draw!")
