import csv

with open("abc.csv","w",newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Course","RollNo"])
    writer.writerow(["Reshma","MCA","28"])
    writer.writerow(["Arya","MCA","08"])
    writer.writerow(["Ananya","MCA","13"])
    writer.writerow(["Prajitha","MCA","26"])

with open("abc.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


