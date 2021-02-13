l=[1,2,4,5,6,3,8]

n=int(input("\nEnter the number: "))
print("\nThe available list is: ",l)

for i in range(0,len(l)):
    if((l[i])==n):
        print("The number is present!")
        break
else:
        print("\nThe number is absent!\n")