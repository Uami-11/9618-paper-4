Animal = [] #1d array with 20 elements of type string
Colour = [] #1d array with 10 elements of type string
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global Animal, Colour, AnimalTopPointer, ColourTopPointer
    if AnimalTopPointer >= 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global Animal, Colour, AnimalTopPointer, ColourTopPointer
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ReturnData
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer -= 1
        return ReturnData


def PushColour(DataToPush):
    global Animal, Colour, AnimalTopPointer, ColourTopPointer
    if ColourTopPointer >= 10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1
        return True

def PopColour():
    global Animal, Colour, AnimalTopPointer, ColourTopPointer
    ReturnData = ""
    if ColourTopPointer == 0:
        return ReturnData
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData

def ReadData():
    global Animal, Colour, AnimalTopPointer, ColourTopPointer

    try:
        AnimalFile = open("AnimalData.txt", 'r')
        AnimalName = AnimalFile.readline().rstrip()
        while AnimalName != "":
            PushAnimal(AnimalName)
            AnimalName = AnimalFile.readline().rstrip()
        AnimalFile.close()

        ColourFile = open("ColourData.txt", 'r')
        ColourName = ColourFile.readline().rstrip()
        while ColourName != "":
            PushColour(ColourName)
            ColourName = ColourFile.readline().rstrip()

    except IOError:
        print("Could not find file.")

def OutputItem():
    ColourName = PopColour()
    AnimalName = PopAnimal()
    Output = True
    if ColourName == "":
        PushAnimal(AnimalName)
        print("No colour")
        Output = False

    if AnimalName == "":
        PushColour(ColourName)
        print("No animal")
        Output = False

    if Output:
        print(ColourName, " ", AnimalName)

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
