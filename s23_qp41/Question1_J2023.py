DataArray = [0]*25

try:
    file = open("Data.txt", 'r')
    for i in range(25):
        DataArray[i] = int(file.readline().rstrip())
    file.close()
except IOError:
    print("File not found.")

def PrintArray(array):
    TheString = ""
    for i in range(25):
        TheString += str(array[i]) + " "
    print(TheString)

PrintArray(DataArray)

def LinearSearch(Array, SearchValue):
    count = 0
    for i in range(25):
        if Array[i] == SearchValue:
            count += 1

    return count

Value = -1
while Value < 0 or Value > 100:
    Value = int(input("Enter a number between 0 and 100: "))
    if Value < 0 or Value > 100:
        print("Number out of range.")

Times = LinearSearch(DataArray, Value)

print("The number ", Value, " is found ", Times, " times.")
