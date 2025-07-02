#Fayldagi barcha ismlarni ekranga chiqaring.

with open("Input/students.txt") as f:
    names = f.read().split()

with open("Ouput/output11.txt","w") as f:
    f.write("\n".join(names))

