#Fayldagi barcha juft sonlarni chiqaring.

# f = open("Input/numbers.txt")

# nums = f.read().split()

# juft = filter(lambda x:int(x % 2==0),nums )

# print(list(juft))


# f2 = open("Output/output04.txt","w")
# f2.write(f"juft sinlar:{juft}")

juftlar = []
with open("Input/numbers.txt") as numbers:
    for number in numbers:
        number = int(number)
        if number % 2 == 0:
            juftlar.append(str(number))
            
with open('Output/output04.txt', 'w') as f:
    f.writelines(", ".join(juftlar))