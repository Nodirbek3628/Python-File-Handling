# Fayldagi barcha sonlarni ekranga chiqaruvchi dastur yozing.

f = open("Input/numbers.txt","r")

nums = f.read()


f2 = open("Output/output01.txt","w")
f2.writelines(nums)

