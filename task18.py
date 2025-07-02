#Ismi “A” harfi bilan boshlanuvchilarni alohida ro‘yxatga oling (`a_names.txt`).

name  = input("ism kiriitng: ").title()

with open('Input/students.txt') as f:
    students = f.read().split()
    if name in students:
            result = f"{name} mavjud "
    else:   
            result = f"{name} mavjud emas "

with open('Ouput/output18.txt','w') as f:
    f.write(f"{students} \n {result}")

