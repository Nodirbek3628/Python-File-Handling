# Sonlar ro‘yxatini tartiblab, `sorted_numbers.txt` fayliga yozing.

file = 'Input/numbers.txt' 

with open(file) as f:
   nums =  f.read().split()
   nums = list(map(int,nums))

   sorted_numberc = sorted(nums)
   sorted_numberc = list(map(str,sorted_numberc))
   

with open('sorted_numbers.txt',"w") as f:
   f.write("Tartiblangan sonlar: "," , ".join(sorted_numberc))


    



    

    

# with open ("Ouput/output10.txt","w") as f:
#     f.write(list(num_order))

#      