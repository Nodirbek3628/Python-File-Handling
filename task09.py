 #Sonlar nechta raqamdan iboratligini (1 xonali, 2 xonali...) aniqlang

file = 'Input/numbers.txt'
xona01 = []
xona02 = []
xona03 = []

with open(file) as f:
    nums = f.read().split()

    for num in nums:
        if int(num) <= 9:
            xona01.append(num)
        elif 10 <= int(num) <= 99:
            xona02.append(num)
        elif 100 <= int(num) <= 999:
            xona03.append(num)
            
xona01.sort(key = lambda x :x)
xona02.sort(key = lambda x:x)
xona03.sort(key = lambda x:x)


with open('Ouput/output09.txt',"w") as f:
    f.writelines(f" {nums}\n 1 xonalik: {xona01},\n 2 xonalik: {xona02},\n 3 xonalik: {xona03}")

