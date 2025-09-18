def func1():
    try:
        l = [1, 2, 3, 4]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error comes")
        return 0
    finally:
        print("Always executed")
t=func1()
print(t)