print("To compute the set of positive integers from the given list of integers")
num_list=[-1,2,3,-3,-4,5]
print("The given list is:",num_list)
print("From the list, the positive integers are:\n")
for i in range(0,len(num_list)):
	if(num_list[i]>=0):
		print(num_list[i])
