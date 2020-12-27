num=[]
n=int(input("Enter the no. of inputs required:"))

for i in range(0,n):
	data=int(input("Enter the no. "))
	num.append(data)

for j in range(0,len(num)):
    if(num[i]>100):
        num[i]='Over'

print(num)