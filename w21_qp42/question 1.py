def Unknown(X,Y):
    if X < Y:
        print(str(X+Y))
        return (Unknown(X+1, Y)*2)
    else:
        if X == Y:
            return 1
        else:
            print(str(X+Y))
            return (Unknown(X-1, Y))//2

#main
def IterativeUnknown(X,Y):
    Total = 1
    while X!= Y:
        print(str(X+Y))
        if X<Y:
            X += 1
            Total *= 2
        else:
            X -= 1
            Total /= 2
    return int(Total)
print("10 and 15")
print(str(IterativeUnknown(10, 15)))
print("10 and 10")
print(str(IterativeUnknown(10, 10)))
print("15 and 10")
print(str(IterativeUnknown(15, 10)))
