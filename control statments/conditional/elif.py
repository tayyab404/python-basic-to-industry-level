age=int(input("Enter your age:"))
if age>=18 and age<=101:
    print("you can vote")
elif age>100:
    print("greater then 100")
elif age<=0:
    print("INvalid age")
else:
    print("error occured")