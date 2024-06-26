# (a)
# declaring the record node
class node:
    def __init__(self, datap, nextp):
        self.data = datap  # integer
        self.nextNode = nextp  # integer


# (b)
# 1d array with all the nodes given in question
linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6),
              node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
# pointers declared with given values
startPointer = 0
emptyList = 5


# (c)
# (i)
def ouputNodes(array, spointer):
    next = spointer
    # looping through the linked list, following the nodes and outputing them
    for i in range(len(array)):
        print(array[next].data)
        next = array[next].nextNode


# (ii)
ouputNodes(linkedList, startPointer)


# (d)
# (ii)
def addNode(array, start, empty):
    add = int(input("Enter data to add: "))

    # checking if there is available space
    if empty < 0 or empty > 9:
        return False
    else:
        # make the inputted data into a node and insert it to the empty space
        newNode = node(add, -1)
        array[empty] = newNode

        previousPointer = 0
        # looping to find the next available space
        while start != -1:
            previousPointer = start
            start = array[start].nextNode
        # making the second last node point to the recently added one
        array[previousPointer].nextNode = empty
        # updating empty list
        empty = array[empty].nextNode
        return True


# (ii)
added = addNode(linkedList, startPointer, emptyList)

if added:
    print("Data added")
else:
    print("Data not added")

ouputNodes(linkedList, startPointer)