x=int(input("Enter the value of x:"))
match x:
    case 0:
        print(" case is zero")
    case 5:
        print( " case is five:")
    case _ if x!=90:
        print(x,"is no 90:")
    case _ if x!=80:
        print(x," is no 80")
    case _:
        print(" case is default:")
