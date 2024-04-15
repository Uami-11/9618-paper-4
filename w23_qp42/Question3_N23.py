import datetime


class Character:
    def __init__(self, Name, DOB, Int, spd):
        self.__CharacterName = Name
        self.__DateOfBirth = DOB
        self.__Intelligence = Int
        self.__Speed = spd

    def GetName(self):
        return self.__CharacterName
    def GetIntelligence(self):
        return self.__Intelligence
    def SetIntelligence(self, NewInt):
        self.__Intelligence = NewInt

    def Learn(self):
        self.SetIntelligence(self.__Intelligence*1.1)
    def ReturnAge(self):
        Age = 2023 - self.__DateOfBirth.year
        return Age
FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)
FirstCharacter.Learn()
Name = FirstCharacter.GetName()
Intel = FirstCharacter.GetIntelligence()
Age = FirstCharacter.ReturnAge()

print(Name, "has an IQ of", Intel, "and is", Age, "years old.")

class MagicCharacter(Character):
    def __init__(self, Name, DOB, Int, spd, el):
        super().__init__(Name, DOB, Int, spd)
        self.__Element = el

    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            super().SetIntelligence(super().GetIntelligence()*1.2)
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence() * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.1)

FirstMagic = MagicCharacter("Light", datetime.datetime(2018, 3, 3), 75, 22, "fire")
FirstMagic.Learn()
Name1 = FirstMagic.GetName()
Intel2 = FirstMagic.GetIntelligence()
Age3 = FirstMagic.ReturnAge()

print(Name1, "has an IQ of", Intel2, ", is", Age3, "years old and controls fire.")
