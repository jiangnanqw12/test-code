import csv

date_list=[]
ning_list=[]
jiao_list=[]

with open('ning_jiao.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    # Skip the header
    next(csv_reader)
    for row in csv_reader:
        date_list.append(row[0])
        ning_list.append(float(row[1]))
        jiao_list.append(float(row[2]))
sum=sum(ning_list)-sum(jiao_list)
print(f"sum:{sum}")