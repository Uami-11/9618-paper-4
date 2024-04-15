global StackData
global StackPointer

StackData = [0]*10
StackPointer = 0

def Output():
    global StackData
    global StackPointer
    for i in range(10):
        print(StackData[i])
    print("Stack Pointer: " + str(StackPointer))

def Push(Item):
    global StackData
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = Item
        StackPointer += 1
        return True

for i in range(11):
    add = int(input("Enter number to add: "))
    pushed = Push(add)
    if pushed:
        print("Number added to stack.")
    else:
        print("Stack is full.")



def Pop():
    global StackData
    global StackPointer

    if StackPointer == 0:
        return -1
    else:
        StackPointer += -1
        Value = StackData[StackPointer]
        return Value

Output()
Pop()
Pop()
Output()