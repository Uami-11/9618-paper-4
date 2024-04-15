#(a)
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8] #array with ten elements from question

#(b)
#(i)
def linearSearch(ToBeFound):
    global arrayData
    for i in range(10):
        if arrayData[i] == ToBeFound:
            return True
        else:
            return False

#(ii)
integr = int(input("Enter number to find: "))
found = linearSearch(integr)

#linearSearch returns boolean
if found:
    print("Number was found")
else:
    print("Number was not found")

#(c)
def bubbleSort():
    global arrayData
    for x in range(10):
        for y in range(9):
            if arrayData[y]<arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp