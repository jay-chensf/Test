def displayNumType(num):
    print(str(num) +" is ",end="")
    if isinstance(num,(int,float,complex,)):
        print("a number of type :" + type(num).__name__)
    else:
        print("not a number at all!!")

displayNumType(-69)
displayNumType(999999999999999999999999999999999999999999)
displayNumType(98.5)
displayNumType(-5.2 + 1.9j)
displayNumType("xxxx")
