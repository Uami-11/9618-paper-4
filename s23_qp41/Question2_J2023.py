class Vehicle:
    def __init__(self, idp, Maxp, IncAmt):
        self.__ID = idp #string
        self.__MaxSpeed = Maxp #integer
        self.__CurrentSpeed = 0 #integer
        self.__IncreaseAmount = IncAmt #integer
        self.__HorizontalPosition = 0 #integer

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, NewSpeed):
        self.__CurrentSpeed = NewSpeed
    def SetHorizontalPosition(self, NewPosition):
        self.__HorizontalPosition = NewPosition

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed
    def OutputInfo(self):
        print("Vehicle is at a horizontal position of ", self.GetHorizontalPosition())
        print("Vehicle is at a speed of ", self.GetCurrentSpeed())

class Helicopter(Vehicle):
    def __init__(self, idp, Maxp, IncAmt, Vertc, Maxh):
        super().__init__(idp, Maxp, IncAmt)
        self.__VerticalPosition = 0 #integer
        self.__VerticalChange = Vertc #integer
        self.__MaxHeight = Maxh #integer

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight

        super().SetCurrentSpeed(super().GetCurrentSpeed() +super().GetIncreaseAmount())
        if super().GetCurrentSpeed() > super().GetMaxSpeed():
            super().SetCurrentSpeed(super().GetMaxSpeed())

        super().SetHorizontalPosition(super().GetHorizontalPosition() + super().GetCurrentSpeed())

    def OutputInfo(self):
        print("Helicopter is at a horizontal position of ", super().GetHorizontalPosition())
        print("Helicopter is at a speed of ", super().GetCurrentSpeed())
        print("Helicopter is at a vertical position of ", self.__VerticalPosition)

TheCar = Vehicle("Tiger", 100, 20)
TheHelicopter = Helicopter("Lion", 350, 40, 3, 100)
TheCar.IncreaseSpeed()
TheCar.IncreaseSpeed()
TheCar.OutputInfo()

TheHelicopter.IncreaseSpeed()
TheHelicopter.IncreaseSpeed()
TheHelicopter.OutputInfo()
