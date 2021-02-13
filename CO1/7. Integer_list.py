num1=[1,2,3,4,5,5,6,2]
num2=[1,2,3,4,5]
print("List1=",num1)
print("List2=",num2)
if(len(num1)==len(num2)):
	print("Equal List Length")
else:
    print("Unqual List Length")
	
num1_sum=0
num2_sum=0
for i in range(0,len(num1)):
	num1_sum=num1_sum+num1[i]
for j in range(0,len(num2)):
	num2_sum=num2_sum+num2[j]
if(num1_sum==num2_sum):
	print("Equal Sum")
else:
    print("Unequal Sum")
