global NameArray
global ScoreArray

NameArray = [""]*11
ScoreArray = [0]*11

def ReadHighScores():
    global NameArray
    global ScoreArray
    try:
        file = open("HighScore.txt", 'r')
        for i in range(10):
            Names = file.readline().strip()
            Scores = int(file.readline().strip())
            NameArray[i] = Names
            ScoreArray[i] = int(Scores)

        file.close()

    except IOError:
        print("Could not find file.")

def OutputHighscore():
    global NameArray
    global ScoreArray
    i = 0
    while i <= 10 and NameArray[i] != "":
        print(str(NameArray[i]) + " " + str(ScoreArray[i]))
        i += 1

ReadHighScores()
OutputHighscore()
UserName = ""
UserScore = 0
while len(UserName) != 3 or (UserScore < 1 or UserScore > 100_000):
    UserName = input("Enter a 3 letter name: ")
    UserScore = int(input("Enter your score: "))
    if len(UserName) != 3:
        print("User name must be 3 characters.")
    if (UserScore < 1 or UserScore > 100_000):
        print("Score must be between 1 and 100,000")


def TopTen(Name, Score):
    global NameArray
    global ScoreArray
    NameArray[10] = Name
    ScoreArray[10] = Score
    for x in range(11):
        for y in range(10):
            if ScoreArray[y] < ScoreArray[y+1]:
                temp1 = ScoreArray[y]
                temp2 = NameArray[y]
                ScoreArray[y] = ScoreArray[y+1]
                NameArray[y] = NameArray[y+1]
                ScoreArray[y+1] = temp1
                NameArray[y+1] = temp2



print("After inserting")
TopTen(UserName, UserScore)
OutputHighscore()

def WriteTopTen():
    newfile = open("NewHighScore.txt", 'w')
    for i in range(10):
        newfile.write(str(NameArray[i])+"\n")
        newfile.write(str(ScoreArray[i])+"\n")
    newfile.close()