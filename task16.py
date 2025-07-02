#Ismi 5 harfdan uzun bo‘lgan talabalarni chiqaring.
with open('Input/students.txt') as f:
    names = f.read().split()
    names =list (map(str,names))

    names_filter = list(filter(lambda name:len(name) > 5 , names))

with open('Ouput/output16.txt','w') as f:
    f.write(f"{names}\n5 ta harfdan uzun bulgan talabalarninng ismi: {names_filter}")
