global Jobs
global NumberOfJobs

def Initialise():
    global Jobs
    global NumberOfJobs
    Jobs = []
    for i in range(100):
        Jobs.append([-1,-1])
    NumberOfJobs = 0

def AddJob(JobNo, Priority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs == 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs][0] = JobNo
        Jobs[NumberOfJobs][1] = Priority
        print("Added")
        NumberOfJobs += 1

Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33,8)
AddJob(12, 9)
AddJob(78, 1)

def InsertionSort():
    global Jobs
    global NumberOfJobs
    for i in range(1, NumberOfJobs):
        current1 = Jobs[i][0]
        current2 = Jobs[i][1]
        while i > 0 and Jobs[i-1][1] > current2:
            Jobs[i][0] = Jobs[i-1][0]
            Jobs[i][1] = Jobs[i-1][1]
            i -= 1
        Jobs[i][0] = current1
        Jobs[i][1] = current2

def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(NumberOfJobs):
        print(str(Jobs[i][0]) + " priority "+ str(Jobs[i][1]))

InsertionSort()
PrintArray()
