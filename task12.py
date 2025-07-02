#Ismlar sonini hisoblang.

with open("Input/students.txt") as f:
    names = f.read().split()
    
with open("Ouput/output12.txt","w") as f:
    f.write(f"ismlar soni: {len(names)} ta ")

   