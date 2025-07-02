#Ismlarni teskari tartibda chiqaring.

f = open("Input/students.txt")

names = f.readlines()
names.sort(reverse=True)


f2 = open("Ouput/output14.txt","w")
f2.writelines(names)

