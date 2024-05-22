def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for X in range(LengthString):
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or (FirstCharacter == 'o') or (FirstCharacter == 'u'):
            Total += 1

        Value = Value[1:]
    return Total

print(IterativeVowels("house"))

def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    else:
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or (FirstCharacter == 'o') or (FirstCharacter == 'u'):
            return 1 + RecursiveVowels(Value[1:])
        else:
            return RecursiveVowels(Value[1:])

print(RecursiveVowels("imagine"))
