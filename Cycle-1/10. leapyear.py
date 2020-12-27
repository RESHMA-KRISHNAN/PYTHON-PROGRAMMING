print("_____LEAP YEAR_____")
a=int(input("Enter the current year:"))
b=int(input("Enter the final year:"))
print("\nThe Leap Years Be:\n")
for c in range(a,b):
   year = list(range(a,b))
for i in range(len(year)):
    if((year[i]%4)==0):
        print(year[i])
