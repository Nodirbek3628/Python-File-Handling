#. Fayldagi sonlar o‘rtachasini (average) hisoblang.

sonlar = []
with open("Input/numbers.txt") as numbers:
    for number in numbers:
        number = int(number)
        sonlar.append(number)
    
ortasi = str(sum(sonlar)/len(sonlar))
print(ortasi)
            
with open("Ouput/output05.txt", 'w') as f:
    f.write(ortasi)
