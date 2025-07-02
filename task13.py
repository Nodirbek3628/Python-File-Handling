#Ismlarni alfavit bo‘yicha tartiblang.

f = open("Input/students.txt")

names = f.readlines()
names.sort()


f2 = open("Ouput/output13.txt","w")
f2.writelines(names)
