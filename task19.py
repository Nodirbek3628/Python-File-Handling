with open("Input/grades.csv") as name:
    names = name.read().splitlines()

natija = []
for i in names:
    if i.strip():
        name, grade = i.split(",")
        natija.append(f"Ism: {name}, Baho: {grade}")

with open("Ouput/output19.txt", "w") as javob:
    javob.write("\n".join(natija))
