Queue = [""] * 50
HeadPointer = -1
TailPointer = 0

def Enqueue(DataToAdd):
    global Queue, HeadPointer, TailPointer

    if TailPointer > 50:
        print("The queue is full.")
    else:
        Queue[TailPointer] = DataToAdd
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0

def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1:
        Value = "Empty"
    else:
        Value = Queue[HeadPointer]
        HeadPointer += 1
    return Value

def ReadData():
    try:
        file = open("QueueData.txt", 'r')
        ID = file.readline().rstrip()
        while ID != "":
            Enqueue(ID)
            ID = file.readline().rstrip()

        file.close
    except IOError:
        print("File not found.")

class RecordData:
    def __init__(self, idp, totalp):
        self.ID = idp
        self.Total = totalp

Records = []
NumberRecords = 0

def TotalData():
    global Records, NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if DataAccessed == "Empty":
        pass
    else:
        if NumberRecords == 0:
            Records.append(RecordData(DataAccessed, 1))
            Flag = True
            NumberRecords += 1
        else:
            for X in range(NumberRecords):
                if Records[X].ID == DataAccessed:
                    Records[X].Total += 1
                    Flag = True

        if Flag == False:
            Records.append(RecordData(DataAccessed, 1))
            NumberRecords += 1

def OutputRecords():
    global Records, NumberRecords
    index = 0
    for i in range(NumberRecords):
        print("ID ", Records[i].ID, " Total ", Records[i].Total)


ReadData()
for i in range(TailPointer):
    TotalData()
OutputRecords()

