QueueArray = [""]*10
HeadPointer = 0
TailPointer = 0
NumberItems = 0

def Enqueue(QueueArray, HeadPointer, TailPointer, NumberItems, DataToAdd):
    if NumberItems == 10:
        return QueueArray, HeadPointer, TailPointer, NumberItems, False
    else:
        QueueArray[NumberItems] = DataToAdd
        if TailPointer >= 9:
            TailPointer = 0
        else:
            TailPointer += 1
        NumberItems += 1
        return QueueArray, HeadPointer, TailPointer, NumberItems,True

def Dequeue(QueueArray, HeadPointer, TailPointer, NumberItems):
    if NumberItems == 0:
        return QueueArray, HeadPointer, TailPointer, NumberItems, "FALSE"
    else:
        Value = QueueArray[HeadPointer]
        HeadPointer += 1
        if HeadPointer >= 9:
            Head = 0
        NumberItems -= 1
        return QueueArray, HeadPointer, TailPointer, NumberItems, Value

for i in range(11):
    Data = input("Enter data to add in queue: ")
    QueueArray, HeadPointer, TailPointer, NumberItems, Added = Enqueue(QueueArray, HeadPointer, TailPointer, NumberItems, Data)
    if Added:
        print("Data was added.")
    else:
        print("Queue is full.")


QueueArray, HeadPointer, TailPointer, NumberItems, Value = Dequeue(QueueArray, HeadPointer, TailPointer, NumberItems)
print(Value)
QueueArray, HeadPointer, TailPointer, NumberItems, Value = Dequeue(QueueArray, HeadPointer, TailPointer, NumberItems)
print(Value)


