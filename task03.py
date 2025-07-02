#Fayldagi eng katta sonni aniqlang.

f = open("Input/numbers.txt")

nums = f.read().split()

max = nums[0]

for num in nums:
    if int(num) > int(max):
        max = num

f2 = open("Output/output03.txt","w")
f2.write(f"max: {max }")