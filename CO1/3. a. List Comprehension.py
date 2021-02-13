print("__To print positive nos in the list using LIST COMPREHENSION__\n")
list = [-1, -2, -3, 4, 5, 6, -10, -21] 
num_list = [num for num in list if num >= 0] 
  
print("Positive numbers in the list: ", num_list)