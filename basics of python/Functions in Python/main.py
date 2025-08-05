def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print("Geometric mean is:", mean)

def isGreater(a, b):
    if a > b:
        print("The first number is greater")
    else:
        print("The second number is greater")
def isless (a,b):
    pass

# Testing with first pair
a = 5
b = 7
calculateGmean(a, b)
isGreater(a, b)

# Testing with second pair
c = 8
d = 20
calculateGmean(c, d)
isGreater(c, d)
