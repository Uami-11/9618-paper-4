class Employee:
    def __init__(self, HourPay, EmpNo, JobT):
        self.__HourlyPay = HourPay
        self.__EmployeeNumber = EmpNo
        self.__JobTitle = JobT
        self.__PayYear2022 = []
        for i in range(52):
            self.__PayYear2022.append(0.0)

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, WeekNo, HoursWorked):
        Pay = self.__HourlyPay * HoursWorked
        self.__PayYear2022[WeekNo - 1] = Pay
    def GetTotalPay(self):
        Pay = 0
        for i in range(52):
            Pay += self.__PayYear2022[i]
        return Pay

class Manager(Employee):
    def __init__(self, HourPay, EmpNo, JobT, Bonus):
        super().__init__(HourPay, EmpNo, JobT)
        self.__BonusValue = Bonus

    def SetPay(self, WeekNo, HoursWorked):
        HoursWorked *= (self.__BonusValue/100) + 1
        super().SetPay(WeekNo, HoursWorked)

EmployeeArray = []
try:
    file = open("Employees.txt", "r")
    HourPay = file.readline().rstrip()
    while HourPay != "":
        HourPay = float(HourPay)
        EmpNo = file.readline().rstrip()
        JobT = file.readline().rstrip()
        try:
            Bonus = float(JobT)
            JobT = file.readline().rstrip()
            TheManagers = Manager(HourPay, EmpNo, JobT, Bonus)
            EmployeeArray.append(TheManagers)

        except:
            TheEmployees = Employee(HourPay, EmpNo, JobT)
            EmployeeArray.append(TheEmployees)
        HourPay = file.readline().rstrip()
    file.close()

except IOError:
    print("404. File not found.")

def EnterHours():
    global EmployeeArray
    try:
        file = open("HoursWeek1.txt", 'r')
        EmpNo = file.readline().rstrip()
        while EmpNo != "":
            found = False
            i = 0
            while not found and i < 8:
                if EmployeeArray[i].GetEmployeeNumber() == EmpNo:
                    HourPay = float(file.readline().rstrip())
                    EmployeeArray[i].SetPay(1, HourPay)
                    found = True
                i += 1
            EmpNo = file.readline().rstrip()
        file.close()
    except IOError:
        print("File not found. :/")

EnterHours()
for i in range(8):
    print(EmployeeArray[i].GetEmployeeNumber() + " " +str(EmployeeArray[i].GetTotalPay()))
