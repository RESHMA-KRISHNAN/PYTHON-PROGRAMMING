print("__To find sum of elements in a list__")
ls=[]
n=int(input("Enter the no. items to be enlisted: "))
for x in range(n):
    data=int(input("Enter the data:"))
    ls.append(data)
list_sum=sum(ls)
print("The sum of the enlisted elements: ",list_sum)