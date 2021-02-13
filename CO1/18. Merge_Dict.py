print("\n_________MERGING OF TWO DICTIONARIES________\n")
dict1 = {'a': 10, 'b': 5, 'c': 3}  
dict2 = {'d': 6, 'e': 4, 'f': 8} 
print("Dictionary 1:\n",dict1)
print("Dictionary 2:\n",dict2)    
dict1.update(dict2)
print("\nAfter performing the update():\n") 
print("dict1 :", dict1) 
print("dict2 :", dict2) 