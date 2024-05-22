import random


class SaleData:
    def __init__(self, idp, quan):
        self.ID = idp #string
        self.Quantity = quan #integer


global CircularQueue #array of 5 elements of type SaleData
global Head #integer
global Tail #integer
global NumberOfItems #integer

CircularQueue = [SaleData("", -1), SaleData("", -1), SaleData("", -1), SaleData("", -1), SaleData("", -1)]
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(NewRecord):
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = NewRecord
        Tail += 1
        if Tail == 5:
            Tail = 0
        NumberOfItems += 1
        return 1

def Dequeue():
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems == 0:
        return SaleData("", -1)
    else:
        ReturnValue = CircularQueue[Head]
        Head += 1
        if Head == 5:
            Head = 0
        NumberOfItems -= 1
        return ReturnValue

def EnterRecord():
    global CircularQueue, Head, Tail, NumberOfItems
    ID = input("Enter ID: ")
    Quantity = int(input("Enter the quantity: "))
    Enqueued = Enqueue(SaleData(ID, Quantity))
    if Enqueued == 1:
        print("Stored")
    else:
        print("Full")

EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
Dequeued = Dequeue()
if Dequeued.ID == "":
    print("There is nothing to dequeue.")
else:
    List = [Dequeued.ID, Dequeued.Quantity]
    Output = random.choice(List)
    print(Output)