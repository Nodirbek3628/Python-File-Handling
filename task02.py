#Fayldagi sonlar yig‘indisini hisoblang.

f = open("Input/numbers.txt")

nums = f.read().split()

s = 0

for num in nums:
    s += int(num)

f2 = open("Output/output02.txt","w")
f2.write(f"sum : {s}")


