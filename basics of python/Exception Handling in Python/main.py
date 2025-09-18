a= input("Enter your number to get the table")
print(f"Multiplication table of {a} is:")
try:
 for i in range(1,11):
    print(f"{int(a)}X{i} = {int(a)*i}")
except:
     print("invalid input")
print("some thing important")
print (" end of the day ")