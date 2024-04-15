class Picture:
    def __init__(self, desc, widthp, heightp, framec):
        self.__Description = desc
        self.__Width = widthp
        self.__Height = heightp
        self.__FrameColour = framec

    def GetDescription(self):
        return self.__Description
    def GetWidth(self):
        return self.__Width
    def GetHeight(self):
        return self.__Height
    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, newdesc):
        self.__Description = newdesc

PictureArray = []
for i in range(100):
    PictureArray.append(Picture("", 0, 0, ""))

def ReadData():
    global PictureArray
    count = 0
    try:
        file = open("Pictures.txt", 'r')
        description = (file.readline()).strip()
        while description != "":
            width = int((file.readline()).strip())
            height = int((file.readline()).strip())
            colour = (file.readline()).strip()
            PictureArray[count] = Picture(description, width, height, colour)
            description = (file.readline()).strip()
            count += 1
        file.close()

    except IOError:
        print("File not found.")
    return count

Number = ReadData()
colourframe = (input("Enter the colour of the frame: ")).lower()
maxwidth = int(input("Enter the maximum width: "))
maxheight = int(input("Enter the maximum height: "))
print("Matching pictures: ")
for i in range(Number):
    if ((PictureArray[i].GetColour()).lower() == colourframe):
        if (PictureArray[i].GetWidth()) <= maxwidth:
            if (PictureArray[i].GetHeight()) <= maxheight:

                print("Description: " + PictureArray[i].GetDescription())
                print("Width: " + str(PictureArray[i].GetWidth()))
                print("Height: " + str(PictureArray[i].GetHeight()))