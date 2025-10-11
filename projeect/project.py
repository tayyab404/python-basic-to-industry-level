Num_1= float(input("Enter the number1 :"))
Num_2= float(input("Enter the number2 :"))
choice=input('Enter your chice = - * % / //')
if choice== '+':
    print(f'addition :{Num_1+num_2}' )
elif choice=='-':
    print(f'subtraction : {Num_1-Num_2}')
elif choice=='*':
    print(f'MUltiplication: {Num_1*Num_2}')
elif choice=='/':
    print(f'Division:{Num_1/Num_2}')
elif choice=='//':
    print(f'float Devision: {Num_1//Num_2}')
else:
    print("Error Occured")