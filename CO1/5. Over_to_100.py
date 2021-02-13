num=[]
n=int(input("Enter the no. of inputs required: "))
for i in range(n):
    data=int(input("Enter the no.:"))
    if data>100:
        num.append("Over")
    else:
	    num.append(data)
print(num)
