
ArrayNodes = []
for i in range(20):
    ArrayNodes.append([-1, -1, -1])

FreeNode = 6
RootPointer = 0
ArrayNodes = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1]]

def SearchValue(Root, ValueToFind):
    global ArrayNodes
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        else:
            if ArrayNodes[Root][1] == -1:
                return -1

    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)

def PostOrder(Root):
    global ArrayNodes
    if ArrayNodes[Root][0] != -1:
        PostOrder(ArrayNodes[Root][0])
    if ArrayNodes[Root][2] != -1:
        PostOrder(ArrayNodes[Root][2])

    print(str(ArrayNodes[Root][1]) + " ")

Position = SearchValue(RootPointer, 15)
if Position == -1:
    print("15 was not found.")
else:
    print("15 was found at Index: " + str(Position))

PostOrder(RootPointer)