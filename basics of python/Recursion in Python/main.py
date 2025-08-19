# Recursion
# User input
n= int(input("enter your number to find the factorial "))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("factorial of",n ,"is:",factorial(n))
# febonacci series
# User input
n=int(input("Enter your number to find thr febunacci series:"))
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
print("The febunacci series of",n,"is:",f(n))
 