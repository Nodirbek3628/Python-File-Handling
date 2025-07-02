#Fayldagi sonlar ichidan 5 ga karralilarni sanang va ularni chiqaring.

file = 'Input/numbers.txt'

with open(file) as f:

    nums = f.read().split()
    multiple = list(filter(lambda x:(int(x) % 5 == 0),nums))
    
with open('Ouput/output08.txt','w') as f:
    f.write(f"{nums} \n 5 ga karrali sonlar {multiple}")