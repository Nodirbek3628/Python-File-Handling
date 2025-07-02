#Har bir baho nechi marta qatnashganini sanang (`Counter` dan foydalaning).
with open("Input/grades.csv") as f:
    f.readline()
    lines = f.read().split()

grades = dict()
for line in lines:
    name, grade = line.split(',')
    if grade not in grades.keys():
        grades[grade] = []
    
    grades[grade].append(name)


with open('Ouput/output23.txt','w') as f:
    f.write(f"{grades}")

