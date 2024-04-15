import random

RandArray = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        RandArray[i][j] = random.randint(1,100)

for i in range(10):
    print(RandArray[i])
print("After sorting:")

for i in range(10):
    for j in range(9):
        for k in range(9-j):
            if RandArray[i][k] > RandArray[i][k+1]:
                temp = RandArray[i][k]
                RandArray[i][k] = RandArray[i][k+1]
                RandArray[i][k+1] = temp
for i in range(10):
    print(RandArray[i])

def BinarySearch(Array, Lower, Upper, Value):
    if Upper >= Lower:
        Mid = int((Lower+Upper-1)/2)
        if Array[0][Mid] == Value:
            return Mid
        else:
            if Array[0][Mid] > Value:
                return BinarySearch(Array, Lower, Mid-1, Value)
            else:
                return BinarySearch(Array, Mid+1, Upper, Value)
    return -1

print("Value to be found: 10")
print("Index found at: " + str(BinarySearch(RandArray, 0, 10, 10)))
print("Value to be found: 0")
print("Index found at: " + str(BinarySearch(RandArray, 0, 10, 0)))