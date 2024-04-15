global StackVowel, StackConstant, VowelTop, ConstantTop
StackVowel = ['']*100
StackConstant = ['']*100

VowelTop = 0
ConstantTop = 0
def PushData(sophin):
    global StackVowel, StackConstant, VowelTop, ConstantTop
    sophin = sophin.lower()
    if sophin == 'a' or sophin == 'e' or sophin == 'i' or sophin == 'o' or sophin == 'u':
        if VowelTop < 101:
            StackVowel[VowelTop] = sophin
            VowelTop += 1
    else:
        if ConstantTop < 101:
            StackConstant[ConstantTop] = sophin
            ConstantTop += 1


def ReaData():
    try:
        file = open("StackData.txt", 'r')
        for i in range(100):
            line = file.readline()[0]
            Pushed = PushData(line)
    except IOError:
        print("404")



