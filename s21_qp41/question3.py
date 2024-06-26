# (a)
class TreasureChest:
    def __init__(self, questionp, answerp, pointsp):
        self.__question = questionp  # as string
        self.__answer = answerp  # as integer
        self.__points = pointsp  # as integer

    # (c)
    # (i)
    def getQuestion(self):
        return self.__question

    # (ii)
    def checkAnswer(self, answer):
        if int(self.__answer) == answer:
            return True
        else:
            return False

    # (iii)
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(int(self.__points) / 2)
        elif attempts == 3 or attempts == 4:
            return int(int(self.__points) / 4)
        else:
            return 0

#(b)

arrayTreasure = [] #1d array of type TreasureChest
def readData():
    global arrayTreasure

    #exception handling
    try:

        file = open("TreasureChestData.txt", 'r') #opening file for reading
        line = (file.readline()).strip() #storing the first line as line and getting rid of whitespace
        #looping until the file is empty/EOF
        while line != "":
            question = line
            answer = (file.readline()).strip()
            points = (file.readline()).strip()
            arrayTreasure.append(TreasureChest(question, answer, points)) #putting all of the values in class and adding it to the array
            line = (file.readline()).strip()
        file.close()

    except IOError:
        print("Could not find file.")

#(c)
#(iv)
readData()
choice = 0
while choice >= 6 or choice <= 0:
    choice = int(input("Enter question number: "))
correct = False
attempts = 0
while not correct:
    answer = int(input(arrayTreasure[choice - 1].getQuestion() + ": "))
    correct = arrayTreasure[choice - 1].checkAnswer(answer)
    attempts = attempts + 1
print(int(arrayTreasure[choice - 1].getPoints(attempts)))