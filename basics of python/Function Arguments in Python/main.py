# def average(a=7,b=2):
#     print("The average is:" ,(a+b)/2)
#     # required function argument
# # average(34,45)
# # default function arguments
# # def average(a=7,b=2):
def average(*number):
    print(type(number))  # number is a tuple
    total = 0
    for i in number:
        total = total + i
    print("Average is:", total / len(number))
    average(5,7)
 

