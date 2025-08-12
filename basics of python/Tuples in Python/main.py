tup=(1,2,3,4,5,"yellow","Pakistan Zindabad")
print(type(tup))
print(tup)
print(tup[0])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[6])

if "yellow" in tup:
    print("jaan")
else:
    print("No jaan") 

if "Roshan Bheela" in tup:
    print("jaan")
else:
    print("No jaan") 
tup2=tup[1:5]
print(tup2)