#`students.txt` faylidagi har bir ism nechta harfdan iboratligini ko‘rsating.

f = open("Input/students.txt")

names =f.read.split()


text = ''
for name in names:
    text += f"{name}: {len(name)}\n"

f2 = open("Output/output15.txt","w")
f2.writelines(text)

