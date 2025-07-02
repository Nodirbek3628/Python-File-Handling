#Fayldagi har bir sonni kvadratga ko‘paytirib ekranga chiqaring.

file = 'Input/numbers.txt'
d = []

with open(file) as f:
    nums = f.read().split()
    kv = map(lambda num:pow(int(num),2),nums)
        

# print(list(kv))
with open('Ouput/output07.txt','w') as f:
    f.write(f" real son:{nums} \n real son kvadrati: {list(kv)}")