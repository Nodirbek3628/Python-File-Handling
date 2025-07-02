#. Fayldagi sonlar o‘rtachasini (average) hisoblang.

with open("Input/numbers.txt") as numbers:
   
    sonlar = list(map(int,numbers))
    
ortasi = str(sum(sonlar)/len(sonlar))
print(ortasi)
            
with open("Ouput/output05.txt", 'w') as f:
    f.write(ortasi)
