# Eng yuqori baho olgan o‘quvchini toping.
with open('Input/grades.csv') as f:
    f.readline()
    lines = f.readlines()

    rows = list(map(lambda line: line.strip().split(','),lines))

    highest_grade = max(rows,key = lambda row:row[1])

with open('Ouput/output21.txt','w') as f:
    f.write(f"{highest_grade}")