# Ismi “A” harfi bilan boshlanuvchilarni alohida ro‘yxatga oling (`a_names.txt`).

with open('Input/students.txt') as f:
    names = f.read().split()
   
    result = []

    for name in names:
        if name[0] == "A":
            result.append(name)

with open('Ouput/output17.txt',"w") as f:
    f.write(" , ".join(result))



    
   

