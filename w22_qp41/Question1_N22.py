global DataArray
DataArray = [0]*100

def ReadFile():
    global DataArray
    try:
        file = open("IntegerData.txt", 'r')
        for i in range(100):
            line = file.readline().strip()
            DataArray[i] = int(line)

    except IOError:
        print("File not found.")

def FindValues():
    global DataArray
    NumberFind = 0
    count = 0
    while NumberFind <1 or NumberFind>100:
        NumberFind = int(input("Enter number between 1 and 100: "))

    for i in range(100):
        if NumberFind == DataArray[i]:
            count += 1
    return count

ReadFile()
NumberTimes = FindValues()
print("It was found " + str(NumberTimes) + " time(s)")

def BubbleSort():
    global DataArray
    for i in range(100):
        for j in range(99):
            if DataArray[j] > DataArray[j+1]:
                temp = DataArray[j]
                DataArray[j] = DataArray[j+1]
                DataArray[j+1] = temp

    print(DataArray)

BubbleSort()