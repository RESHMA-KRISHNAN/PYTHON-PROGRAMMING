import csv
field_names=['ROLLNO','NAME','COURSE']

data=[{'ROLLNO':101,'NAME':'Arya','COURSE':'MCA'},{'ROLLNO':102,'NAME':'Sreelekshmi','COURSE':'MCA'},{'ROLLNO':103,'NAME':'Reshma','COURSE':'MCA'}]
with open('Data.csv','w', newline='')as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(data)


with open('Data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)