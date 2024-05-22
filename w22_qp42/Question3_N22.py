Queue = [0] * 100
HeadPointer = -1
TailPointer = 0

def Enqueue(num):
    global Queue, HeadPointer, TailPointer
    if TailPointer == 100:
        return False
    else:
        Queue[TailPointer] = num
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0
        return True

for i in range(20):
    Enqueued = Enqueue(i + 1)

if Enqueued:
    print("All the values were stored.")

else:
    print("All the values were not stored.")

def RecursiveOutput(Start):
    if Start == 0:
        return Queue[Start]
    else:
        return Queue[Start] + RecursiveOutput(Start-1)

Output = RecursiveOutput(TailPointer - 1)
print(Output)