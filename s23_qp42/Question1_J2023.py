global Animals #array with 10 elements of type string

Animals = []
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")
print(Animals)

def SortDescending():
    global Animals
    ArrayLength = len(Animals)
    for x in range(ArrayLength-1):
        for y in range(ArrayLength-x-1):
            if Animals[y][0] < Animals[y+1][0]:
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = temp

SortDescending()
for i in range(10):
    print(Animals[i])

