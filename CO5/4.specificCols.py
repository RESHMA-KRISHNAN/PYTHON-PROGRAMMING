import csv
with open("data.csv","w",newline='') as file:
  write=csv.writer(file)
  write.writerow(["RollNo","Name","Score"])
  write.writerow(["1","Arya","8.5"])
  write.writerow(["2","Arjun","7"])
  write.writerow(["3","Binsha","7"])
  write.writerow(["4","Calvin","9"])
  write.writerow(["5","Divya","6.5"])
with open("data.csv") as csvfile:
 col=csv.DictReader(csvfile)
 for x in col:
     print(x['RollNo'],x['Score'])