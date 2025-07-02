#Fayldagi barcha toq sonlarni yangi `odd_numbers.txt` fayliga yozing.

file = 'Input/numbers.txt'
toq_son = []

with open(file) as f:
    nums = f.read().split()

    for num in nums:
        if int(num) % 2 != 0:
            toq_son.append(int(num))
 
with open('odd_numbers.txt','w') as f:
    f.write(f"toq sonlar: {toq_son}")

     

 
