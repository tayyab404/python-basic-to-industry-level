a=int(input(" Enter any value between 5 and 10"))
if(a<5 or a>9):
    raise ValueError("your number should be in between 5 and 10")