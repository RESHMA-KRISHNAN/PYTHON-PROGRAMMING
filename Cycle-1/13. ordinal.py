print("___To display ordinal of each element in the given string____")
name="reshma"
print("The given string is: ",name)
print("The ordinals are:")
name_list=list(name)
for i in range(0,len(name_list)):
    print(ord(name_list[i]))