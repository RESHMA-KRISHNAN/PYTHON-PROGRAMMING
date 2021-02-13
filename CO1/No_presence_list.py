l=[1,2,4,5,6,3,8]

n=int(input("\nEnter the number: "))

for i in range(0,len(l)):
    if((l[i])==n):
        flag=1
        break
    else:
        flag=0
print("\nThe available list is: ",l)
if(flag==1):
    print("\nThe number entered is present in the list")
else:
    print("\nThe number entered is absent in the list")


